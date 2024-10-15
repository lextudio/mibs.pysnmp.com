# SNMP MIB module (ETH-OPT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ETH-OPT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:40:53 2024
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class MacAddress(OctetString):
    """Custom type MacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )





class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Codex_ObjectIdentity = ObjectIdentity
codex = _Codex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449)
)
_CdxProductSpecific_ObjectIdentity = ObjectIdentity
cdxProductSpecific = _CdxProductSpecific_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2)
)
_Cdx6500_ObjectIdentity = ObjectIdentity
cdx6500 = _Cdx6500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1)
)
_Cdx6500Configuration_ObjectIdentity = ObjectIdentity
cdx6500Configuration = _Cdx6500Configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2)
)
_Cdx6500CfgProtocolGroup_ObjectIdentity = ObjectIdentity
cdx6500CfgProtocolGroup = _Cdx6500CfgProtocolGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1)
)
_Cdx6500PCTPortProtocolGroup_ObjectIdentity = ObjectIdentity
cdx6500PCTPortProtocolGroup = _Cdx6500PCTPortProtocolGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1)
)
_Cdx6500PPCTdot3PortTable_Object = MibTable
cdx6500PPCTdot3PortTable = _Cdx6500PPCTdot3PortTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 8)
)
if mibBuilder.loadTexts:
    cdx6500PPCTdot3PortTable.setStatus("mandatory")
_Cdx6500PPCTdot3PortEntry_Object = MibTableRow
cdx6500PPCTdot3PortEntry = _Cdx6500PPCTdot3PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 8, 1)
)
cdx6500PPCTdot3PortEntry.setIndexNames(
    (0, "ETH-OPT-MIB", "cdx6500dot3IfIndex"),
)
if mibBuilder.loadTexts:
    cdx6500PPCTdot3PortEntry.setStatus("mandatory")
_Cdx6500dot3IfIndex_Type = Integer32
_Cdx6500dot3IfIndex_Object = MibTableColumn
cdx6500dot3IfIndex = _Cdx6500dot3IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 8, 1, 1),
    _Cdx6500dot3IfIndex_Type()
)
cdx6500dot3IfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500dot3IfIndex.setStatus("mandatory")


class _Cdx6500dot3LanCableType_Type(Integer32):
    """Custom type cdx6500dot3LanCableType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("aui", 2),
          ("utp", 3))
    )


_Cdx6500dot3LanCableType_Type.__name__ = "Integer32"
_Cdx6500dot3LanCableType_Object = MibTableColumn
cdx6500dot3LanCableType = _Cdx6500dot3LanCableType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 8, 1, 2),
    _Cdx6500dot3LanCableType_Type()
)
cdx6500dot3LanCableType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500dot3LanCableType.setStatus("mandatory")
_Cdx6500dot3PortMacAddress_Type = MacAddress
_Cdx6500dot3PortMacAddress_Object = MibTableColumn
cdx6500dot3PortMacAddress = _Cdx6500dot3PortMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 8, 1, 3),
    _Cdx6500dot3PortMacAddress_Type()
)
cdx6500dot3PortMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500dot3PortMacAddress.setStatus("mandatory")
_Cdx6500dot3TransmitQueueLimit_Type = Integer32
_Cdx6500dot3TransmitQueueLimit_Object = MibTableColumn
cdx6500dot3TransmitQueueLimit = _Cdx6500dot3TransmitQueueLimit_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 8, 1, 4),
    _Cdx6500dot3TransmitQueueLimit_Type()
)
cdx6500dot3TransmitQueueLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500dot3TransmitQueueLimit.setStatus("mandatory")
_Cdx6500dot3CollisionSensitivity_Type = Integer32
_Cdx6500dot3CollisionSensitivity_Object = MibTableColumn
cdx6500dot3CollisionSensitivity = _Cdx6500dot3CollisionSensitivity_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 8, 1, 5),
    _Cdx6500dot3CollisionSensitivity_Type()
)
cdx6500dot3CollisionSensitivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500dot3CollisionSensitivity.setStatus("mandatory")
_Cdx6500dot3CarrierSensitivity_Type = Integer32
_Cdx6500dot3CarrierSensitivity_Object = MibTableColumn
cdx6500dot3CarrierSensitivity = _Cdx6500dot3CarrierSensitivity_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 8, 1, 6),
    _Cdx6500dot3CarrierSensitivity_Type()
)
cdx6500dot3CarrierSensitivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500dot3CarrierSensitivity.setStatus("mandatory")
_Cdx6500dot3BridgeLinkNum_Type = Integer32
_Cdx6500dot3BridgeLinkNum_Object = MibTableColumn
cdx6500dot3BridgeLinkNum = _Cdx6500dot3BridgeLinkNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 8, 1, 7),
    _Cdx6500dot3BridgeLinkNum_Type()
)
cdx6500dot3BridgeLinkNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500dot3BridgeLinkNum.setStatus("mandatory")
_Cdx6500dot3RouterIfNum_Type = Integer32
_Cdx6500dot3RouterIfNum_Object = MibTableColumn
cdx6500dot3RouterIfNum = _Cdx6500dot3RouterIfNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 8, 1, 8),
    _Cdx6500dot3RouterIfNum_Type()
)
cdx6500dot3RouterIfNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500dot3RouterIfNum.setStatus("mandatory")


class _Cdx6500dot3DuplexMode_Type(Integer32):
    """Custom type cdx6500dot3DuplexMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("full", 1),
          ("half", 0))
    )


_Cdx6500dot3DuplexMode_Type.__name__ = "Integer32"
_Cdx6500dot3DuplexMode_Object = MibTableColumn
cdx6500dot3DuplexMode = _Cdx6500dot3DuplexMode_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 8, 1, 9),
    _Cdx6500dot3DuplexMode_Type()
)
cdx6500dot3DuplexMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500dot3DuplexMode.setStatus("mandatory")
_Cdx6500Statistics_ObjectIdentity = ObjectIdentity
cdx6500Statistics = _Cdx6500Statistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3)
)
_Cdx6500StatProtocolGroup_ObjectIdentity = ObjectIdentity
cdx6500StatProtocolGroup = _Cdx6500StatProtocolGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1)
)
_Cdx6500PSTPortProtocolGroup_ObjectIdentity = ObjectIdentity
cdx6500PSTPortProtocolGroup = _Cdx6500PSTPortProtocolGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1)
)
_Cdx6500PPSTdot3PortTable_Object = MibTable
cdx6500PPSTdot3PortTable = _Cdx6500PPSTdot3PortTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 8)
)
if mibBuilder.loadTexts:
    cdx6500PPSTdot3PortTable.setStatus("mandatory")
_Cdx6500PPSTdot3PortEntry_Object = MibTableRow
cdx6500PPSTdot3PortEntry = _Cdx6500PPSTdot3PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 8, 1)
)
cdx6500PPSTdot3PortEntry.setIndexNames(
    (0, "ETH-OPT-MIB", "cdx6500dot3StatsIfIndex"),
)
if mibBuilder.loadTexts:
    cdx6500PPSTdot3PortEntry.setStatus("mandatory")
_Cdx6500dot3StatsIfIndex_Type = Integer32
_Cdx6500dot3StatsIfIndex_Object = MibTableColumn
cdx6500dot3StatsIfIndex = _Cdx6500dot3StatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 8, 1, 1),
    _Cdx6500dot3StatsIfIndex_Type()
)
cdx6500dot3StatsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500dot3StatsIfIndex.setStatus("mandatory")


class _Cdx6500dot3StatsPortType_Type(Integer32):
    """Custom type cdx6500dot3StatsPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            30
        )
    )
    namedValues = NamedValues(
        ("eth", 30)
    )


_Cdx6500dot3StatsPortType_Type.__name__ = "Integer32"
_Cdx6500dot3StatsPortType_Object = MibTableColumn
cdx6500dot3StatsPortType = _Cdx6500dot3StatsPortType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 8, 1, 2),
    _Cdx6500dot3StatsPortType_Type()
)
cdx6500dot3StatsPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500dot3StatsPortType.setStatus("mandatory")
_Cdx6500dot3StatsRxShortFrames_Type = Counter32
_Cdx6500dot3StatsRxShortFrames_Object = MibTableColumn
cdx6500dot3StatsRxShortFrames = _Cdx6500dot3StatsRxShortFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 8, 1, 3),
    _Cdx6500dot3StatsRxShortFrames_Type()
)
cdx6500dot3StatsRxShortFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500dot3StatsRxShortFrames.setStatus("mandatory")
_Cdx6500dot3StatsRxCollisions_Type = Counter32
_Cdx6500dot3StatsRxCollisions_Object = MibTableColumn
cdx6500dot3StatsRxCollisions = _Cdx6500dot3StatsRxCollisions_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 8, 1, 4),
    _Cdx6500dot3StatsRxCollisions_Type()
)
cdx6500dot3StatsRxCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500dot3StatsRxCollisions.setStatus("mandatory")
_Cdx6500dot3StatsRxLongFrames_Type = Counter32
_Cdx6500dot3StatsRxLongFrames_Object = MibTableColumn
cdx6500dot3StatsRxLongFrames = _Cdx6500dot3StatsRxLongFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 8, 1, 5),
    _Cdx6500dot3StatsRxLongFrames_Type()
)
cdx6500dot3StatsRxLongFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500dot3StatsRxLongFrames.setStatus("mandatory")
_Cdx6500dot3StatsTxDiscards_Type = Counter32
_Cdx6500dot3StatsTxDiscards_Object = MibTableColumn
cdx6500dot3StatsTxDiscards = _Cdx6500dot3StatsTxDiscards_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 8, 1, 6),
    _Cdx6500dot3StatsTxDiscards_Type()
)
cdx6500dot3StatsTxDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500dot3StatsTxDiscards.setStatus("mandatory")
_Cdx6500dot3StatsDataBytesRx_Type = Counter32
_Cdx6500dot3StatsDataBytesRx_Object = MibTableColumn
cdx6500dot3StatsDataBytesRx = _Cdx6500dot3StatsDataBytesRx_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 8, 1, 7),
    _Cdx6500dot3StatsDataBytesRx_Type()
)
cdx6500dot3StatsDataBytesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500dot3StatsDataBytesRx.setStatus("mandatory")
_Cdx6500dot3StatsDataBytesTx_Type = Counter32
_Cdx6500dot3StatsDataBytesTx_Object = MibTableColumn
cdx6500dot3StatsDataBytesTx = _Cdx6500dot3StatsDataBytesTx_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 8, 1, 8),
    _Cdx6500dot3StatsDataBytesTx_Type()
)
cdx6500dot3StatsDataBytesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500dot3StatsDataBytesTx.setStatus("mandatory")


class _Cdx6500dot3StatsPortStatus_Type(Integer32):
    """Custom type cdx6500dot3StatsPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3,
              4,
              50)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("down", 4),
          ("enabled", 1),
          ("newvalDisabled", 50),
          ("up", 3))
    )


_Cdx6500dot3StatsPortStatus_Type.__name__ = "Integer32"
_Cdx6500dot3StatsPortStatus_Object = MibTableColumn
cdx6500dot3StatsPortStatus = _Cdx6500dot3StatsPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 8, 1, 9),
    _Cdx6500dot3StatsPortStatus_Type()
)
cdx6500dot3StatsPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500dot3StatsPortStatus.setStatus("mandatory")
_Cdx6500dot3StatsLastStatReset_Type = DisplayString
_Cdx6500dot3StatsLastStatReset_Object = MibTableColumn
cdx6500dot3StatsLastStatReset = _Cdx6500dot3StatsLastStatReset_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 8, 1, 10),
    _Cdx6500dot3StatsLastStatReset_Type()
)
cdx6500dot3StatsLastStatReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500dot3StatsLastStatReset.setStatus("mandatory")


class _Cdx6500dot3StatsClearStats_Type(Integer32):
    """Custom type cdx6500dot3StatsClearStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_Cdx6500dot3StatsClearStats_Type.__name__ = "Integer32"
_Cdx6500dot3StatsClearStats_Object = MibTableColumn
cdx6500dot3StatsClearStats = _Cdx6500dot3StatsClearStats_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 8, 1, 11),
    _Cdx6500dot3StatsClearStats_Type()
)
cdx6500dot3StatsClearStats.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cdx6500dot3StatsClearStats.setStatus("mandatory")


class _Cdx6500dot3StatsCommand_Type(Integer32):
    """Custom type cdx6500dot3StatsCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("boot", 2),
          ("disable", 3),
          ("enable", 1))
    )


_Cdx6500dot3StatsCommand_Type.__name__ = "Integer32"
_Cdx6500dot3StatsCommand_Object = MibTableColumn
cdx6500dot3StatsCommand = _Cdx6500dot3StatsCommand_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 8, 1, 12),
    _Cdx6500dot3StatsCommand_Type()
)
cdx6500dot3StatsCommand.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cdx6500dot3StatsCommand.setStatus("mandatory")
_Cdx6500dot3Statsframesin_Type = Counter32
_Cdx6500dot3Statsframesin_Object = MibTableColumn
cdx6500dot3Statsframesin = _Cdx6500dot3Statsframesin_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 8, 1, 13),
    _Cdx6500dot3Statsframesin_Type()
)
cdx6500dot3Statsframesin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500dot3Statsframesin.setStatus("mandatory")
_Cdx6500dot3Statsframesout_Type = Counter32
_Cdx6500dot3Statsframesout_Object = MibTableColumn
cdx6500dot3Statsframesout = _Cdx6500dot3Statsframesout_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 8, 1, 14),
    _Cdx6500dot3Statsframesout_Type()
)
cdx6500dot3Statsframesout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500dot3Statsframesout.setStatus("mandatory")
_Cdx6500dot3Statsfpsin_Type = Counter32
_Cdx6500dot3Statsfpsin_Object = MibTableColumn
cdx6500dot3Statsfpsin = _Cdx6500dot3Statsfpsin_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 8, 1, 15),
    _Cdx6500dot3Statsfpsin_Type()
)
cdx6500dot3Statsfpsin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500dot3Statsfpsin.setStatus("mandatory")
_Cdx6500dot3Statsfpsout_Type = Counter32
_Cdx6500dot3Statsfpsout_Object = MibTableColumn
cdx6500dot3Statsfpsout = _Cdx6500dot3Statsfpsout_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 8, 1, 16),
    _Cdx6500dot3Statsfpsout_Type()
)
cdx6500dot3Statsfpsout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500dot3Statsfpsout.setStatus("mandatory")
_Cdx6500dot3Statshadiscards_Type = Counter32
_Cdx6500dot3Statshadiscards_Object = MibTableColumn
cdx6500dot3Statshadiscards = _Cdx6500dot3Statshadiscards_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 8, 1, 17),
    _Cdx6500dot3Statshadiscards_Type()
)
cdx6500dot3Statshadiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500dot3Statshadiscards.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ETH-OPT-MIB",
    **{"MacAddress": MacAddress,
       "DisplayString": DisplayString,
       "codex": codex,
       "cdxProductSpecific": cdxProductSpecific,
       "cdx6500": cdx6500,
       "cdx6500Configuration": cdx6500Configuration,
       "cdx6500CfgProtocolGroup": cdx6500CfgProtocolGroup,
       "cdx6500PCTPortProtocolGroup": cdx6500PCTPortProtocolGroup,
       "cdx6500PPCTdot3PortTable": cdx6500PPCTdot3PortTable,
       "cdx6500PPCTdot3PortEntry": cdx6500PPCTdot3PortEntry,
       "cdx6500dot3IfIndex": cdx6500dot3IfIndex,
       "cdx6500dot3LanCableType": cdx6500dot3LanCableType,
       "cdx6500dot3PortMacAddress": cdx6500dot3PortMacAddress,
       "cdx6500dot3TransmitQueueLimit": cdx6500dot3TransmitQueueLimit,
       "cdx6500dot3CollisionSensitivity": cdx6500dot3CollisionSensitivity,
       "cdx6500dot3CarrierSensitivity": cdx6500dot3CarrierSensitivity,
       "cdx6500dot3BridgeLinkNum": cdx6500dot3BridgeLinkNum,
       "cdx6500dot3RouterIfNum": cdx6500dot3RouterIfNum,
       "cdx6500dot3DuplexMode": cdx6500dot3DuplexMode,
       "cdx6500Statistics": cdx6500Statistics,
       "cdx6500StatProtocolGroup": cdx6500StatProtocolGroup,
       "cdx6500PSTPortProtocolGroup": cdx6500PSTPortProtocolGroup,
       "cdx6500PPSTdot3PortTable": cdx6500PPSTdot3PortTable,
       "cdx6500PPSTdot3PortEntry": cdx6500PPSTdot3PortEntry,
       "cdx6500dot3StatsIfIndex": cdx6500dot3StatsIfIndex,
       "cdx6500dot3StatsPortType": cdx6500dot3StatsPortType,
       "cdx6500dot3StatsRxShortFrames": cdx6500dot3StatsRxShortFrames,
       "cdx6500dot3StatsRxCollisions": cdx6500dot3StatsRxCollisions,
       "cdx6500dot3StatsRxLongFrames": cdx6500dot3StatsRxLongFrames,
       "cdx6500dot3StatsTxDiscards": cdx6500dot3StatsTxDiscards,
       "cdx6500dot3StatsDataBytesRx": cdx6500dot3StatsDataBytesRx,
       "cdx6500dot3StatsDataBytesTx": cdx6500dot3StatsDataBytesTx,
       "cdx6500dot3StatsPortStatus": cdx6500dot3StatsPortStatus,
       "cdx6500dot3StatsLastStatReset": cdx6500dot3StatsLastStatReset,
       "cdx6500dot3StatsClearStats": cdx6500dot3StatsClearStats,
       "cdx6500dot3StatsCommand": cdx6500dot3StatsCommand,
       "cdx6500dot3Statsframesin": cdx6500dot3Statsframesin,
       "cdx6500dot3Statsframesout": cdx6500dot3Statsframesout,
       "cdx6500dot3Statsfpsin": cdx6500dot3Statsfpsin,
       "cdx6500dot3Statsfpsout": cdx6500dot3Statsfpsout,
       "cdx6500dot3Statshadiscards": cdx6500dot3Statshadiscards}
)
