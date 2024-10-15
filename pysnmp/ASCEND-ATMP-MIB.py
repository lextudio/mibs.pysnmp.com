# SNMP MIB module (ASCEND-ATMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-ATMP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:40:53 2024
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

(DisplayString,
 atmpGroup) = mibBuilder.importSymbols(
    "ASCEND-MIB",
    "DisplayString",
    "atmpGroup")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _AtmpAgentMode_Type(Integer32):
    """Custom type atmpAgentMode based on Integer32"""
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
        *(("atmp-disabled", 1),
          ("both-agent", 4),
          ("foreign-agent", 3),
          ("home-agent", 2))
    )


_AtmpAgentMode_Type.__name__ = "Integer32"
_AtmpAgentMode_Object = MibScalar
atmpAgentMode = _AtmpAgentMode_Object(
    (1, 3, 6, 1, 4, 1, 529, 24, 1),
    _AtmpAgentMode_Type()
)
atmpAgentMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpAgentMode.setStatus("mandatory")


class _AtmpAgentType_Type(Integer32):
    """Custom type atmpAgentType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ha-gateway", 2),
          ("ha-notapp", 3),
          ("ha-router", 1))
    )


_AtmpAgentType_Type.__name__ = "Integer32"
_AtmpAgentType_Object = MibScalar
atmpAgentType = _AtmpAgentType_Object(
    (1, 3, 6, 1, 4, 1, 529, 24, 2),
    _AtmpAgentType_Type()
)
atmpAgentType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpAgentType.setStatus("mandatory")
_AtmpAgentUDPPort_Type = Integer32
_AtmpAgentUDPPort_Object = MibScalar
atmpAgentUDPPort = _AtmpAgentUDPPort_Object(
    (1, 3, 6, 1, 4, 1, 529, 24, 3),
    _AtmpAgentUDPPort_Type()
)
atmpAgentUDPPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpAgentUDPPort.setStatus("mandatory")


class _AtmpAgentGreMtu_Type(Integer32):
    """Custom type atmpAgentGreMtu based on Integer32"""
    defaultValue = 0


_AtmpAgentGreMtu_Object = MibScalar
atmpAgentGreMtu = _AtmpAgentGreMtu_Object(
    (1, 3, 6, 1, 4, 1, 529, 24, 4),
    _AtmpAgentGreMtu_Type()
)
atmpAgentGreMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpAgentGreMtu.setStatus("mandatory")


class _AtmpAgentForceFragmentation_Type(Integer32):
    """Custom type atmpAgentForceFragmentation based on Integer32"""
    defaultValue = 2

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


_AtmpAgentForceFragmentation_Type.__name__ = "Integer32"
_AtmpAgentForceFragmentation_Object = MibScalar
atmpAgentForceFragmentation = _AtmpAgentForceFragmentation_Object(
    (1, 3, 6, 1, 4, 1, 529, 24, 5),
    _AtmpAgentForceFragmentation_Type()
)
atmpAgentForceFragmentation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpAgentForceFragmentation.setStatus("mandatory")
_AtmpAgentHAIdleLimit_Type = Integer32
_AtmpAgentHAIdleLimit_Object = MibScalar
atmpAgentHAIdleLimit = _AtmpAgentHAIdleLimit_Object(
    (1, 3, 6, 1, 4, 1, 529, 24, 6),
    _AtmpAgentHAIdleLimit_Type()
)
atmpAgentHAIdleLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpAgentHAIdleLimit.setStatus("mandatory")


class _AtmpLastErrorGenerated_Type(Integer32):
    """Custom type atmpLastErrorGenerated based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("bad-tunnel", 6),
          ("dns-failed", 9),
          ("err-general", 10),
          ("err-parameter", 5),
          ("err-timeout", 7),
          ("fa-auth-failed", 2),
          ("ha-atmp-disabled", 3),
          ("hn-unreachable", 8),
          ("no-error", 1),
          ("too-many-tunnel", 4))
    )


_AtmpLastErrorGenerated_Type.__name__ = "Integer32"
_AtmpLastErrorGenerated_Object = MibScalar
atmpLastErrorGenerated = _AtmpLastErrorGenerated_Object(
    (1, 3, 6, 1, 4, 1, 529, 24, 7),
    _AtmpLastErrorGenerated_Type()
)
atmpLastErrorGenerated.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmpLastErrorGenerated.setStatus("mandatory")
_AtmpAgentSentErrorTo_Type = IpAddress
_AtmpAgentSentErrorTo_Object = MibScalar
atmpAgentSentErrorTo = _AtmpAgentSentErrorTo_Object(
    (1, 3, 6, 1, 4, 1, 529, 24, 8),
    _AtmpAgentSentErrorTo_Type()
)
atmpAgentSentErrorTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpAgentSentErrorTo.setStatus("mandatory")


class _AtmpLastErrorRecv_Type(Integer32):
    """Custom type atmpLastErrorRecv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("bad-tunnel", 6),
          ("err-parameter", 5),
          ("err-timeout", 7),
          ("fa-auth-failed", 2),
          ("ha-atmp-disabled", 3),
          ("hn-unreachable", 8),
          ("no-error", 1),
          ("too-many-tunnel", 4))
    )


_AtmpLastErrorRecv_Type.__name__ = "Integer32"
_AtmpLastErrorRecv_Object = MibScalar
atmpLastErrorRecv = _AtmpLastErrorRecv_Object(
    (1, 3, 6, 1, 4, 1, 529, 24, 9),
    _AtmpLastErrorRecv_Type()
)
atmpLastErrorRecv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmpLastErrorRecv.setStatus("mandatory")
_AtmpAgentRecvErrorFrom_Type = IpAddress
_AtmpAgentRecvErrorFrom_Object = MibScalar
atmpAgentRecvErrorFrom = _AtmpAgentRecvErrorFrom_Object(
    (1, 3, 6, 1, 4, 1, 529, 24, 10),
    _AtmpAgentRecvErrorFrom_Type()
)
atmpAgentRecvErrorFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpAgentRecvErrorFrom.setStatus("mandatory")


class _AtmpEnableAtmpTraps_Type(Integer32):
    """Custom type atmpEnableAtmpTraps based on Integer32"""
    defaultValue = 2

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


_AtmpEnableAtmpTraps_Type.__name__ = "Integer32"
_AtmpEnableAtmpTraps_Object = MibScalar
atmpEnableAtmpTraps = _AtmpEnableAtmpTraps_Object(
    (1, 3, 6, 1, 4, 1, 529, 24, 11),
    _AtmpEnableAtmpTraps_Type()
)
atmpEnableAtmpTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmpEnableAtmpTraps.setStatus("mandatory")
_AtmpAgentNumberFATunnels_Type = Integer32
_AtmpAgentNumberFATunnels_Object = MibScalar
atmpAgentNumberFATunnels = _AtmpAgentNumberFATunnels_Object(
    (1, 3, 6, 1, 4, 1, 529, 24, 12),
    _AtmpAgentNumberFATunnels_Type()
)
atmpAgentNumberFATunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpAgentNumberFATunnels.setStatus("mandatory")
_AtmpAgentNumberHATunnels_Type = Integer32
_AtmpAgentNumberHATunnels_Object = MibScalar
atmpAgentNumberHATunnels = _AtmpAgentNumberHATunnels_Object(
    (1, 3, 6, 1, 4, 1, 529, 24, 13),
    _AtmpAgentNumberHATunnels_Type()
)
atmpAgentNumberHATunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpAgentNumberHATunnels.setStatus("mandatory")
_AtmpAgentNumberLocalTunnels_Type = Integer32
_AtmpAgentNumberLocalTunnels_Object = MibScalar
atmpAgentNumberLocalTunnels = _AtmpAgentNumberLocalTunnels_Object(
    (1, 3, 6, 1, 4, 1, 529, 24, 14),
    _AtmpAgentNumberLocalTunnels_Type()
)
atmpAgentNumberLocalTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpAgentNumberLocalTunnels.setStatus("mandatory")
_AtmpAgentTunnelHighWater_Type = Integer32
_AtmpAgentTunnelHighWater_Object = MibScalar
atmpAgentTunnelHighWater = _AtmpAgentTunnelHighWater_Object(
    (1, 3, 6, 1, 4, 1, 529, 24, 15),
    _AtmpAgentTunnelHighWater_Type()
)
atmpAgentTunnelHighWater.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpAgentTunnelHighWater.setStatus("mandatory")
_AtmpTunnelTable_Object = MibTable
atmpTunnelTable = _AtmpTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 24, 16)
)
if mibBuilder.loadTexts:
    atmpTunnelTable.setStatus("mandatory")
_AtmpTunnelEntry_Object = MibTableRow
atmpTunnelEntry = _AtmpTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 24, 16, 1)
)
atmpTunnelEntry.setIndexNames(
    (0, "ASCEND-ATMP-MIB", "atmpTunnelIndex"),
)
if mibBuilder.loadTexts:
    atmpTunnelEntry.setStatus("mandatory")


class _AtmpTunnelIndex_Type(Integer32):
    """Custom type atmpTunnelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AtmpTunnelIndex_Type.__name__ = "Integer32"
_AtmpTunnelIndex_Object = MibTableColumn
atmpTunnelIndex = _AtmpTunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 24, 16, 1, 1),
    _AtmpTunnelIndex_Type()
)
atmpTunnelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpTunnelIndex.setStatus("mandatory")


class _AtmpTunnelId_Type(Integer32):
    """Custom type atmpTunnelId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AtmpTunnelId_Type.__name__ = "Integer32"
_AtmpTunnelId_Object = MibTableColumn
atmpTunnelId = _AtmpTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 529, 24, 16, 1, 2),
    _AtmpTunnelId_Type()
)
atmpTunnelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpTunnelId.setStatus("mandatory")
_AtmpHAIpAddress_Type = IpAddress
_AtmpHAIpAddress_Object = MibTableColumn
atmpHAIpAddress = _AtmpHAIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 529, 24, 16, 1, 3),
    _AtmpHAIpAddress_Type()
)
atmpHAIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpHAIpAddress.setStatus("mandatory")
_AtmpFAIpAddress_Type = IpAddress
_AtmpFAIpAddress_Object = MibTableColumn
atmpFAIpAddress = _AtmpFAIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 529, 24, 16, 1, 4),
    _AtmpFAIpAddress_Type()
)
atmpFAIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpFAIpAddress.setStatus("mandatory")


class _AtmpTunneledProtocol_Type(Integer32):
    """Custom type atmpTunneledProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ip", 1),
          ("ipx", 2))
    )


_AtmpTunneledProtocol_Type.__name__ = "Integer32"
_AtmpTunneledProtocol_Object = MibTableColumn
atmpTunneledProtocol = _AtmpTunneledProtocol_Object(
    (1, 3, 6, 1, 4, 1, 529, 24, 16, 1, 5),
    _AtmpTunneledProtocol_Type()
)
atmpTunneledProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpTunneledProtocol.setStatus("mandatory")


class _AtmpTunnelType_Type(Integer32):
    """Custom type atmpTunnelType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("fa", 2),
          ("ha", 1))
    )


_AtmpTunnelType_Type.__name__ = "Integer32"
_AtmpTunnelType_Object = MibTableColumn
atmpTunnelType = _AtmpTunnelType_Object(
    (1, 3, 6, 1, 4, 1, 529, 24, 16, 1, 6),
    _AtmpTunnelType_Type()
)
atmpTunnelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpTunnelType.setStatus("mandatory")


class _AtmpTunnelState_Type(Integer32):
    """Custom type atmpTunnelState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 3),
          ("registering", 1),
          ("up", 2))
    )


_AtmpTunnelState_Type.__name__ = "Integer32"
_AtmpTunnelState_Object = MibTableColumn
atmpTunnelState = _AtmpTunnelState_Object(
    (1, 3, 6, 1, 4, 1, 529, 24, 16, 1, 7),
    _AtmpTunnelState_Type()
)
atmpTunnelState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpTunnelState.setStatus("mandatory")
_AtmpMnIpAddress_Type = IpAddress
_AtmpMnIpAddress_Object = MibTableColumn
atmpMnIpAddress = _AtmpMnIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 529, 24, 16, 1, 8),
    _AtmpMnIpAddress_Type()
)
atmpMnIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpMnIpAddress.setStatus("mandatory")
_AtmpMnNetmask_Type = IpAddress
_AtmpMnNetmask_Object = MibTableColumn
atmpMnNetmask = _AtmpMnNetmask_Object(
    (1, 3, 6, 1, 4, 1, 529, 24, 16, 1, 9),
    _AtmpMnNetmask_Type()
)
atmpMnNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpMnNetmask.setStatus("mandatory")


class _AtmpMnIpxNetAddress_Type(OctetString):
    """Custom type atmpMnIpxNetAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_AtmpMnIpxNetAddress_Type.__name__ = "OctetString"
_AtmpMnIpxNetAddress_Object = MibTableColumn
atmpMnIpxNetAddress = _AtmpMnIpxNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 529, 24, 16, 1, 10),
    _AtmpMnIpxNetAddress_Type()
)
atmpMnIpxNetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpMnIpxNetAddress.setStatus("mandatory")


class _AtmpMnIpxNodeAddress_Type(OctetString):
    """Custom type atmpMnIpxNodeAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_AtmpMnIpxNodeAddress_Type.__name__ = "OctetString"
_AtmpMnIpxNodeAddress_Object = MibTableColumn
atmpMnIpxNodeAddress = _AtmpMnIpxNodeAddress_Object(
    (1, 3, 6, 1, 4, 1, 529, 24, 16, 1, 11),
    _AtmpMnIpxNodeAddress_Type()
)
atmpMnIpxNodeAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpMnIpxNodeAddress.setStatus("mandatory")
_AtmpHNProfileName_Type = DisplayString
_AtmpHNProfileName_Object = MibTableColumn
atmpHNProfileName = _AtmpHNProfileName_Object(
    (1, 3, 6, 1, 4, 1, 529, 24, 16, 1, 12),
    _AtmpHNProfileName_Type()
)
atmpHNProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpHNProfileName.setStatus("mandatory")
_AtmpHNMaxTunnels_Type = Integer32
_AtmpHNMaxTunnels_Object = MibTableColumn
atmpHNMaxTunnels = _AtmpHNMaxTunnels_Object(
    (1, 3, 6, 1, 4, 1, 529, 24, 16, 1, 13),
    _AtmpHNMaxTunnels_Type()
)
atmpHNMaxTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpHNMaxTunnels.setStatus("mandatory")
_AtmpFAPrimaryHAAddress_Type = DisplayString
_AtmpFAPrimaryHAAddress_Object = MibTableColumn
atmpFAPrimaryHAAddress = _AtmpFAPrimaryHAAddress_Object(
    (1, 3, 6, 1, 4, 1, 529, 24, 16, 1, 14),
    _AtmpFAPrimaryHAAddress_Type()
)
atmpFAPrimaryHAAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpFAPrimaryHAAddress.setStatus("mandatory")
_AtmpFASecondaryHAAddress_Type = DisplayString
_AtmpFASecondaryHAAddress_Object = MibTableColumn
atmpFASecondaryHAAddress = _AtmpFASecondaryHAAddress_Object(
    (1, 3, 6, 1, 4, 1, 529, 24, 16, 1, 15),
    _AtmpFASecondaryHAAddress_Type()
)
atmpFASecondaryHAAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpFASecondaryHAAddress.setStatus("mandatory")
_AtmpFASsnStatusIndex_Type = Integer32
_AtmpFASsnStatusIndex_Object = MibTableColumn
atmpFASsnStatusIndex = _AtmpFASsnStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 24, 16, 1, 16),
    _AtmpFASsnStatusIndex_Type()
)
atmpFASsnStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpFASsnStatusIndex.setStatus("mandatory")
_AtmpFAUserName_Type = DisplayString
_AtmpFAUserName_Object = MibTableColumn
atmpFAUserName = _AtmpFAUserName_Object(
    (1, 3, 6, 1, 4, 1, 529, 24, 16, 1, 17),
    _AtmpFAUserName_Type()
)
atmpFAUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpFAUserName.setStatus("mandatory")
_AtmpInPkts_Type = Counter32
_AtmpInPkts_Object = MibTableColumn
atmpInPkts = _AtmpInPkts_Object(
    (1, 3, 6, 1, 4, 1, 529, 24, 16, 1, 18),
    _AtmpInPkts_Type()
)
atmpInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpInPkts.setStatus("mandatory")
_AtmpInOctets_Type = Counter32
_AtmpInOctets_Object = MibTableColumn
atmpInOctets = _AtmpInOctets_Object(
    (1, 3, 6, 1, 4, 1, 529, 24, 16, 1, 19),
    _AtmpInOctets_Type()
)
atmpInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpInOctets.setStatus("mandatory")
_AtmpInErrPkts_Type = Counter32
_AtmpInErrPkts_Object = MibTableColumn
atmpInErrPkts = _AtmpInErrPkts_Object(
    (1, 3, 6, 1, 4, 1, 529, 24, 16, 1, 20),
    _AtmpInErrPkts_Type()
)
atmpInErrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpInErrPkts.setStatus("mandatory")
_AtmpOutPkts_Type = Counter32
_AtmpOutPkts_Object = MibTableColumn
atmpOutPkts = _AtmpOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 529, 24, 16, 1, 21),
    _AtmpOutPkts_Type()
)
atmpOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpOutPkts.setStatus("mandatory")
_AtmpOutOctets_Type = Counter32
_AtmpOutOctets_Object = MibTableColumn
atmpOutOctets = _AtmpOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 529, 24, 16, 1, 22),
    _AtmpOutOctets_Type()
)
atmpOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpOutOctets.setStatus("mandatory")
_AtmpOutErrPkts_Type = Counter32
_AtmpOutErrPkts_Object = MibTableColumn
atmpOutErrPkts = _AtmpOutErrPkts_Object(
    (1, 3, 6, 1, 4, 1, 529, 24, 16, 1, 23),
    _AtmpOutErrPkts_Type()
)
atmpOutErrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpOutErrPkts.setStatus("mandatory")
_AtmpPktsForcedToFragment_Type = Counter32
_AtmpPktsForcedToFragment_Object = MibTableColumn
atmpPktsForcedToFragment = _AtmpPktsForcedToFragment_Object(
    (1, 3, 6, 1, 4, 1, 529, 24, 16, 1, 24),
    _AtmpPktsForcedToFragment_Type()
)
atmpPktsForcedToFragment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpPktsForcedToFragment.setStatus("mandatory")
_AtmpPktsFailedFragment_Type = Counter32
_AtmpPktsFailedFragment_Object = MibTableColumn
atmpPktsFailedFragment = _AtmpPktsFailedFragment_Object(
    (1, 3, 6, 1, 4, 1, 529, 24, 16, 1, 25),
    _AtmpPktsFailedFragment_Type()
)
atmpPktsFailedFragment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpPktsFailedFragment.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-ATMP-MIB",
    **{"atmpAgentMode": atmpAgentMode,
       "atmpAgentType": atmpAgentType,
       "atmpAgentUDPPort": atmpAgentUDPPort,
       "atmpAgentGreMtu": atmpAgentGreMtu,
       "atmpAgentForceFragmentation": atmpAgentForceFragmentation,
       "atmpAgentHAIdleLimit": atmpAgentHAIdleLimit,
       "atmpLastErrorGenerated": atmpLastErrorGenerated,
       "atmpAgentSentErrorTo": atmpAgentSentErrorTo,
       "atmpLastErrorRecv": atmpLastErrorRecv,
       "atmpAgentRecvErrorFrom": atmpAgentRecvErrorFrom,
       "atmpEnableAtmpTraps": atmpEnableAtmpTraps,
       "atmpAgentNumberFATunnels": atmpAgentNumberFATunnels,
       "atmpAgentNumberHATunnels": atmpAgentNumberHATunnels,
       "atmpAgentNumberLocalTunnels": atmpAgentNumberLocalTunnels,
       "atmpAgentTunnelHighWater": atmpAgentTunnelHighWater,
       "atmpTunnelTable": atmpTunnelTable,
       "atmpTunnelEntry": atmpTunnelEntry,
       "atmpTunnelIndex": atmpTunnelIndex,
       "atmpTunnelId": atmpTunnelId,
       "atmpHAIpAddress": atmpHAIpAddress,
       "atmpFAIpAddress": atmpFAIpAddress,
       "atmpTunneledProtocol": atmpTunneledProtocol,
       "atmpTunnelType": atmpTunnelType,
       "atmpTunnelState": atmpTunnelState,
       "atmpMnIpAddress": atmpMnIpAddress,
       "atmpMnNetmask": atmpMnNetmask,
       "atmpMnIpxNetAddress": atmpMnIpxNetAddress,
       "atmpMnIpxNodeAddress": atmpMnIpxNodeAddress,
       "atmpHNProfileName": atmpHNProfileName,
       "atmpHNMaxTunnels": atmpHNMaxTunnels,
       "atmpFAPrimaryHAAddress": atmpFAPrimaryHAAddress,
       "atmpFASecondaryHAAddress": atmpFASecondaryHAAddress,
       "atmpFASsnStatusIndex": atmpFASsnStatusIndex,
       "atmpFAUserName": atmpFAUserName,
       "atmpInPkts": atmpInPkts,
       "atmpInOctets": atmpInOctets,
       "atmpInErrPkts": atmpInErrPkts,
       "atmpOutPkts": atmpOutPkts,
       "atmpOutOctets": atmpOutOctets,
       "atmpOutErrPkts": atmpOutErrPkts,
       "atmpPktsForcedToFragment": atmpPktsForcedToFragment,
       "atmpPktsFailedFragment": atmpPktsFailedFragment}
)
