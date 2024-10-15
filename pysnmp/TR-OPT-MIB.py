# SNMP MIB module (TR-OPT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TR-OPT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:07:16 2024
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
_Cdx6500PPCTdot5PortTable_Object = MibTable
cdx6500PPCTdot5PortTable = _Cdx6500PPCTdot5PortTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 9)
)
if mibBuilder.loadTexts:
    cdx6500PPCTdot5PortTable.setStatus("mandatory")
_Cdx6500PPCTdot5PortEntry_Object = MibTableRow
cdx6500PPCTdot5PortEntry = _Cdx6500PPCTdot5PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 9, 1)
)
cdx6500PPCTdot5PortEntry.setIndexNames(
    (0, "TR-OPT-MIB", "cdx6500dot5IfIndex"),
)
if mibBuilder.loadTexts:
    cdx6500PPCTdot5PortEntry.setStatus("mandatory")
_Cdx6500dot5IfIndex_Type = Integer32
_Cdx6500dot5IfIndex_Object = MibTableColumn
cdx6500dot5IfIndex = _Cdx6500dot5IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 9, 1, 1),
    _Cdx6500dot5IfIndex_Type()
)
cdx6500dot5IfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500dot5IfIndex.setStatus("mandatory")


class _Cdx6500dot5LanCableType_Type(Integer32):
    """Custom type cdx6500dot5LanCableType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3,
              50)
        )
    )
    namedValues = NamedValues(
        *(("newvalUtp", 50),
          ("stp", 1),
          ("unknown", 3),
          ("utp", 0))
    )


_Cdx6500dot5LanCableType_Type.__name__ = "Integer32"
_Cdx6500dot5LanCableType_Object = MibTableColumn
cdx6500dot5LanCableType = _Cdx6500dot5LanCableType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 9, 1, 2),
    _Cdx6500dot5LanCableType_Type()
)
cdx6500dot5LanCableType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500dot5LanCableType.setStatus("mandatory")
_Cdx6500dot5PortMacAddress_Type = MacAddress
_Cdx6500dot5PortMacAddress_Object = MibTableColumn
cdx6500dot5PortMacAddress = _Cdx6500dot5PortMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 9, 1, 3),
    _Cdx6500dot5PortMacAddress_Type()
)
cdx6500dot5PortMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500dot5PortMacAddress.setStatus("mandatory")
_Cdx6500dot5LocalRingNumber_Type = Integer32
_Cdx6500dot5LocalRingNumber_Object = MibTableColumn
cdx6500dot5LocalRingNumber = _Cdx6500dot5LocalRingNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 9, 1, 4),
    _Cdx6500dot5LocalRingNumber_Type()
)
cdx6500dot5LocalRingNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500dot5LocalRingNumber.setStatus("mandatory")


class _Cdx6500dot5EarlyTokenRelease_Type(Integer32):
    """Custom type cdx6500dot5EarlyTokenRelease based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              50)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1),
          ("newvalDisable", 50))
    )


_Cdx6500dot5EarlyTokenRelease_Type.__name__ = "Integer32"
_Cdx6500dot5EarlyTokenRelease_Object = MibTableColumn
cdx6500dot5EarlyTokenRelease = _Cdx6500dot5EarlyTokenRelease_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 9, 1, 5),
    _Cdx6500dot5EarlyTokenRelease_Type()
)
cdx6500dot5EarlyTokenRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500dot5EarlyTokenRelease.setStatus("mandatory")
_Cdx6500dot5TransmitQueueLimit_Type = Integer32
_Cdx6500dot5TransmitQueueLimit_Object = MibTableColumn
cdx6500dot5TransmitQueueLimit = _Cdx6500dot5TransmitQueueLimit_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 9, 1, 6),
    _Cdx6500dot5TransmitQueueLimit_Type()
)
cdx6500dot5TransmitQueueLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500dot5TransmitQueueLimit.setStatus("mandatory")
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
_Cdx6500PPSTdot5PortTable_Object = MibTable
cdx6500PPSTdot5PortTable = _Cdx6500PPSTdot5PortTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 9)
)
if mibBuilder.loadTexts:
    cdx6500PPSTdot5PortTable.setStatus("mandatory")
_Cdx6500PPSTdot5PortEntry_Object = MibTableRow
cdx6500PPSTdot5PortEntry = _Cdx6500PPSTdot5PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 9, 1)
)
cdx6500PPSTdot5PortEntry.setIndexNames(
    (0, "TR-OPT-MIB", "cdx6500dot5StatsIfIndex"),
)
if mibBuilder.loadTexts:
    cdx6500PPSTdot5PortEntry.setStatus("mandatory")
_Cdx6500dot5StatsIfIndex_Type = Integer32
_Cdx6500dot5StatsIfIndex_Object = MibTableColumn
cdx6500dot5StatsIfIndex = _Cdx6500dot5StatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 9, 1, 1),
    _Cdx6500dot5StatsIfIndex_Type()
)
cdx6500dot5StatsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500dot5StatsIfIndex.setStatus("mandatory")


class _Cdx6500dot5StatsPortType_Type(Integer32):
    """Custom type cdx6500dot5StatsPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            28
        )
    )
    namedValues = NamedValues(
        ("tr", 28)
    )


_Cdx6500dot5StatsPortType_Type.__name__ = "Integer32"
_Cdx6500dot5StatsPortType_Object = MibTableColumn
cdx6500dot5StatsPortType = _Cdx6500dot5StatsPortType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 9, 1, 2),
    _Cdx6500dot5StatsPortType_Type()
)
cdx6500dot5StatsPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500dot5StatsPortType.setStatus("mandatory")
_Cdx6500dot5StatsDataBytesRx_Type = Counter32
_Cdx6500dot5StatsDataBytesRx_Object = MibTableColumn
cdx6500dot5StatsDataBytesRx = _Cdx6500dot5StatsDataBytesRx_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 9, 1, 3),
    _Cdx6500dot5StatsDataBytesRx_Type()
)
cdx6500dot5StatsDataBytesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500dot5StatsDataBytesRx.setStatus("mandatory")
_Cdx6500dot5StatsDataBytesTx_Type = Counter32
_Cdx6500dot5StatsDataBytesTx_Object = MibTableColumn
cdx6500dot5StatsDataBytesTx = _Cdx6500dot5StatsDataBytesTx_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 9, 1, 4),
    _Cdx6500dot5StatsDataBytesTx_Type()
)
cdx6500dot5StatsDataBytesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500dot5StatsDataBytesTx.setStatus("mandatory")
_Cdx6500dot5StatsFrameSizeExc_Type = Counter32
_Cdx6500dot5StatsFrameSizeExc_Object = MibTableColumn
cdx6500dot5StatsFrameSizeExc = _Cdx6500dot5StatsFrameSizeExc_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 9, 1, 5),
    _Cdx6500dot5StatsFrameSizeExc_Type()
)
cdx6500dot5StatsFrameSizeExc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500dot5StatsFrameSizeExc.setStatus("mandatory")
_Cdx6500dot5StatsShortFrames_Type = Counter32
_Cdx6500dot5StatsShortFrames_Object = MibTableColumn
cdx6500dot5StatsShortFrames = _Cdx6500dot5StatsShortFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 9, 1, 6),
    _Cdx6500dot5StatsShortFrames_Type()
)
cdx6500dot5StatsShortFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500dot5StatsShortFrames.setStatus("mandatory")
_Cdx6500dot5StatsTransmitDiscards_Type = Counter32
_Cdx6500dot5StatsTransmitDiscards_Object = MibTableColumn
cdx6500dot5StatsTransmitDiscards = _Cdx6500dot5StatsTransmitDiscards_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 9, 1, 7),
    _Cdx6500dot5StatsTransmitDiscards_Type()
)
cdx6500dot5StatsTransmitDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500dot5StatsTransmitDiscards.setStatus("mandatory")


class _Cdx6500dot5StatsPortStatus_Type(Integer32):
    """Custom type cdx6500dot5StatsPortStatus based on Integer32"""
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


_Cdx6500dot5StatsPortStatus_Type.__name__ = "Integer32"
_Cdx6500dot5StatsPortStatus_Object = MibTableColumn
cdx6500dot5StatsPortStatus = _Cdx6500dot5StatsPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 9, 1, 8),
    _Cdx6500dot5StatsPortStatus_Type()
)
cdx6500dot5StatsPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500dot5StatsPortStatus.setStatus("mandatory")
_Cdx6500dot5StatsLastStatReset_Type = DisplayString
_Cdx6500dot5StatsLastStatReset_Object = MibTableColumn
cdx6500dot5StatsLastStatReset = _Cdx6500dot5StatsLastStatReset_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 9, 1, 9),
    _Cdx6500dot5StatsLastStatReset_Type()
)
cdx6500dot5StatsLastStatReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500dot5StatsLastStatReset.setStatus("mandatory")


class _Cdx6500dot5StatsClearStats_Type(Integer32):
    """Custom type cdx6500dot5StatsClearStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_Cdx6500dot5StatsClearStats_Type.__name__ = "Integer32"
_Cdx6500dot5StatsClearStats_Object = MibTableColumn
cdx6500dot5StatsClearStats = _Cdx6500dot5StatsClearStats_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 9, 1, 10),
    _Cdx6500dot5StatsClearStats_Type()
)
cdx6500dot5StatsClearStats.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cdx6500dot5StatsClearStats.setStatus("mandatory")
_Cdx6500Controls_ObjectIdentity = ObjectIdentity
cdx6500Controls = _Cdx6500Controls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TR-OPT-MIB",
    **{"MacAddress": MacAddress,
       "DisplayString": DisplayString,
       "codex": codex,
       "cdxProductSpecific": cdxProductSpecific,
       "cdx6500": cdx6500,
       "cdx6500Configuration": cdx6500Configuration,
       "cdx6500CfgProtocolGroup": cdx6500CfgProtocolGroup,
       "cdx6500PCTPortProtocolGroup": cdx6500PCTPortProtocolGroup,
       "cdx6500PPCTdot5PortTable": cdx6500PPCTdot5PortTable,
       "cdx6500PPCTdot5PortEntry": cdx6500PPCTdot5PortEntry,
       "cdx6500dot5IfIndex": cdx6500dot5IfIndex,
       "cdx6500dot5LanCableType": cdx6500dot5LanCableType,
       "cdx6500dot5PortMacAddress": cdx6500dot5PortMacAddress,
       "cdx6500dot5LocalRingNumber": cdx6500dot5LocalRingNumber,
       "cdx6500dot5EarlyTokenRelease": cdx6500dot5EarlyTokenRelease,
       "cdx6500dot5TransmitQueueLimit": cdx6500dot5TransmitQueueLimit,
       "cdx6500Statistics": cdx6500Statistics,
       "cdx6500StatProtocolGroup": cdx6500StatProtocolGroup,
       "cdx6500PSTPortProtocolGroup": cdx6500PSTPortProtocolGroup,
       "cdx6500PPSTdot5PortTable": cdx6500PPSTdot5PortTable,
       "cdx6500PPSTdot5PortEntry": cdx6500PPSTdot5PortEntry,
       "cdx6500dot5StatsIfIndex": cdx6500dot5StatsIfIndex,
       "cdx6500dot5StatsPortType": cdx6500dot5StatsPortType,
       "cdx6500dot5StatsDataBytesRx": cdx6500dot5StatsDataBytesRx,
       "cdx6500dot5StatsDataBytesTx": cdx6500dot5StatsDataBytesTx,
       "cdx6500dot5StatsFrameSizeExc": cdx6500dot5StatsFrameSizeExc,
       "cdx6500dot5StatsShortFrames": cdx6500dot5StatsShortFrames,
       "cdx6500dot5StatsTransmitDiscards": cdx6500dot5StatsTransmitDiscards,
       "cdx6500dot5StatsPortStatus": cdx6500dot5StatsPortStatus,
       "cdx6500dot5StatsLastStatReset": cdx6500dot5StatsLastStatReset,
       "cdx6500dot5StatsClearStats": cdx6500dot5StatsClearStats,
       "cdx6500Controls": cdx6500Controls}
)
