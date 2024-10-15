# SNMP MIB module (PACKETPOWER-EG4-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PACKETPOWER-EG4-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:36:12 2024
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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Org_ObjectIdentity = ObjectIdentity
org = _Org_ObjectIdentity(
    (1, 3)
)
_Dod_ObjectIdentity = ObjectIdentity
dod = _Dod_ObjectIdentity(
    (1, 3, 6)
)
_Internet_ObjectIdentity = ObjectIdentity
internet = _Internet_ObjectIdentity(
    (1, 3, 6, 1)
)
_Private_ObjectIdentity = ObjectIdentity
private = _Private_ObjectIdentity(
    (1, 3, 6, 1, 4)
)
_Enterprises_ObjectIdentity = ObjectIdentity
enterprises = _Enterprises_ObjectIdentity(
    (1, 3, 6, 1, 4, 1)
)
_PacketPower_ObjectIdentity = ObjectIdentity
packetPower = _PacketPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33688)
)
_Eg4_ObjectIdentity = ObjectIdentity
eg4 = _Eg4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33688, 4)
)
_ReadingsTable_Object = MibTable
readingsTable = _ReadingsTable_Object(
    (1, 3, 6, 1, 4, 1, 33688, 4, 1)
)
if mibBuilder.loadTexts:
    readingsTable.setStatus("current")
_ReadingsEntry_Object = MibTableRow
readingsEntry = _ReadingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 33688, 4, 1, 1)
)
readingsEntry.setIndexNames(
    (0, "PACKETPOWER-EG4-MIB", "reNodeId1"),
    (0, "PACKETPOWER-EG4-MIB", "reNodeId2"),
    (0, "PACKETPOWER-EG4-MIB", "reNodeId3"),
    (0, "PACKETPOWER-EG4-MIB", "reNodeId4"),
    (0, "PACKETPOWER-EG4-MIB", "channelId"),
)
if mibBuilder.loadTexts:
    readingsEntry.setStatus("current")


class _ReNodeId1_Type(Integer32):
    """Custom type reNodeId1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_ReNodeId1_Type.__name__ = "Integer32"
_ReNodeId1_Object = MibTableColumn
reNodeId1 = _ReNodeId1_Object(
    (1, 3, 6, 1, 4, 1, 33688, 4, 1, 1, 1),
    _ReNodeId1_Type()
)
reNodeId1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    reNodeId1.setStatus("current")


class _ReNodeId2_Type(Integer32):
    """Custom type reNodeId2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_ReNodeId2_Type.__name__ = "Integer32"
_ReNodeId2_Object = MibTableColumn
reNodeId2 = _ReNodeId2_Object(
    (1, 3, 6, 1, 4, 1, 33688, 4, 1, 1, 2),
    _ReNodeId2_Type()
)
reNodeId2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    reNodeId2.setStatus("current")


class _ReNodeId3_Type(Integer32):
    """Custom type reNodeId3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_ReNodeId3_Type.__name__ = "Integer32"
_ReNodeId3_Object = MibTableColumn
reNodeId3 = _ReNodeId3_Object(
    (1, 3, 6, 1, 4, 1, 33688, 4, 1, 1, 3),
    _ReNodeId3_Type()
)
reNodeId3.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    reNodeId3.setStatus("current")


class _ReNodeId4_Type(Integer32):
    """Custom type reNodeId4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_ReNodeId4_Type.__name__ = "Integer32"
_ReNodeId4_Object = MibTableColumn
reNodeId4 = _ReNodeId4_Object(
    (1, 3, 6, 1, 4, 1, 33688, 4, 1, 1, 4),
    _ReNodeId4_Type()
)
reNodeId4.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    reNodeId4.setStatus("current")


class _ChannelId_Type(Integer32):
    """Custom type channelId based on Integer32"""
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
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("battery", 10),
          ("contact", 12),
          ("contactcount", 13),
          ("current", 2),
          ("energy", 4),
          ("frequency", 5),
          ("humidity", 7),
          ("power", 3),
          ("pressure", 11),
          ("temperature", 6),
          ("va", 8),
          ("vdd", 9),
          ("voltage", 1))
    )


_ChannelId_Type.__name__ = "Integer32"
_ChannelId_Object = MibTableColumn
channelId = _ChannelId_Object(
    (1, 3, 6, 1, 4, 1, 33688, 4, 1, 1, 5),
    _ChannelId_Type()
)
channelId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    channelId.setStatus("current")


class _ReNodeIdHex_Type(DisplayString):
    """Custom type reNodeIdHex based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ReNodeIdHex_Type.__name__ = "DisplayString"
_ReNodeIdHex_Object = MibTableColumn
reNodeIdHex = _ReNodeIdHex_Object(
    (1, 3, 6, 1, 4, 1, 33688, 4, 1, 1, 6),
    _ReNodeIdHex_Type()
)
reNodeIdHex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reNodeIdHex.setStatus("current")


class _ReNodeIdString_Type(DisplayString):
    """Custom type reNodeIdString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_ReNodeIdString_Type.__name__ = "DisplayString"
_ReNodeIdString_Object = MibTableColumn
reNodeIdString = _ReNodeIdString_Object(
    (1, 3, 6, 1, 4, 1, 33688, 4, 1, 1, 7),
    _ReNodeIdString_Type()
)
reNodeIdString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reNodeIdString.setStatus("current")


class _ReChannelName_Type(DisplayString):
    """Custom type reChannelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ReChannelName_Type.__name__ = "DisplayString"
_ReChannelName_Object = MibTableColumn
reChannelName = _ReChannelName_Object(
    (1, 3, 6, 1, 4, 1, 33688, 4, 1, 1, 8),
    _ReChannelName_Type()
)
reChannelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reChannelName.setStatus("current")
_ReTime_Type = DateAndTime
_ReTime_Object = MibTableColumn
reTime = _ReTime_Object(
    (1, 3, 6, 1, 4, 1, 33688, 4, 1, 1, 9),
    _ReTime_Type()
)
reTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reTime.setStatus("current")


class _ReUnixTime_Type(Integer32):
    """Custom type reUnixTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_ReUnixTime_Type.__name__ = "Integer32"
_ReUnixTime_Object = MibTableColumn
reUnixTime = _ReUnixTime_Object(
    (1, 3, 6, 1, 4, 1, 33688, 4, 1, 1, 10),
    _ReUnixTime_Type()
)
reUnixTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reUnixTime.setStatus("current")


class _ReIso8601Time_Type(DisplayString):
    """Custom type reIso8601Time based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ReIso8601Time_Type.__name__ = "DisplayString"
_ReIso8601Time_Object = MibTableColumn
reIso8601Time = _ReIso8601Time_Object(
    (1, 3, 6, 1, 4, 1, 33688, 4, 1, 1, 11),
    _ReIso8601Time_Type()
)
reIso8601Time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reIso8601Time.setStatus("current")


class _ReValue_Type(Integer32):
    """Custom type reValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_ReValue_Type.__name__ = "Integer32"
_ReValue_Object = MibTableColumn
reValue = _ReValue_Object(
    (1, 3, 6, 1, 4, 1, 33688, 4, 1, 1, 12),
    _ReValue_Type()
)
reValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reValue.setStatus("current")


class _ReUnits_Type(DisplayString):
    """Custom type reUnits based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ReUnits_Type.__name__ = "DisplayString"
_ReUnits_Object = MibTableColumn
reUnits = _ReUnits_Object(
    (1, 3, 6, 1, 4, 1, 33688, 4, 1, 1, 13),
    _ReUnits_Type()
)
reUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reUnits.setStatus("current")
_NodesTable_Object = MibTable
nodesTable = _NodesTable_Object(
    (1, 3, 6, 1, 4, 1, 33688, 4, 2)
)
if mibBuilder.loadTexts:
    nodesTable.setStatus("current")
_NodesEntry_Object = MibTableRow
nodesEntry = _NodesEntry_Object(
    (1, 3, 6, 1, 4, 1, 33688, 4, 2, 1)
)
nodesEntry.setIndexNames(
    (0, "PACKETPOWER-EG4-MIB", "ntNodeId1"),
    (0, "PACKETPOWER-EG4-MIB", "ntNodeId2"),
    (0, "PACKETPOWER-EG4-MIB", "ntNodeId3"),
    (0, "PACKETPOWER-EG4-MIB", "ntNodeId4"),
)
if mibBuilder.loadTexts:
    nodesEntry.setStatus("current")


class _NtNodeId1_Type(Integer32):
    """Custom type ntNodeId1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65532),
    )


_NtNodeId1_Type.__name__ = "Integer32"
_NtNodeId1_Object = MibTableColumn
ntNodeId1 = _NtNodeId1_Object(
    (1, 3, 6, 1, 4, 1, 33688, 4, 2, 1, 1),
    _NtNodeId1_Type()
)
ntNodeId1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntNodeId1.setStatus("current")


class _NtNodeId2_Type(Integer32):
    """Custom type ntNodeId2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65532),
    )


_NtNodeId2_Type.__name__ = "Integer32"
_NtNodeId2_Object = MibTableColumn
ntNodeId2 = _NtNodeId2_Object(
    (1, 3, 6, 1, 4, 1, 33688, 4, 2, 1, 2),
    _NtNodeId2_Type()
)
ntNodeId2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntNodeId2.setStatus("current")


class _NtNodeId3_Type(Integer32):
    """Custom type ntNodeId3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65532),
    )


_NtNodeId3_Type.__name__ = "Integer32"
_NtNodeId3_Object = MibTableColumn
ntNodeId3 = _NtNodeId3_Object(
    (1, 3, 6, 1, 4, 1, 33688, 4, 2, 1, 3),
    _NtNodeId3_Type()
)
ntNodeId3.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntNodeId3.setStatus("current")


class _NtNodeId4_Type(Integer32):
    """Custom type ntNodeId4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65532),
    )


_NtNodeId4_Type.__name__ = "Integer32"
_NtNodeId4_Object = MibTableColumn
ntNodeId4 = _NtNodeId4_Object(
    (1, 3, 6, 1, 4, 1, 33688, 4, 2, 1, 4),
    _NtNodeId4_Type()
)
ntNodeId4.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntNodeId4.setStatus("current")


class _NtNodeIdHex_Type(DisplayString):
    """Custom type ntNodeIdHex based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_NtNodeIdHex_Type.__name__ = "DisplayString"
_NtNodeIdHex_Object = MibTableColumn
ntNodeIdHex = _NtNodeIdHex_Object(
    (1, 3, 6, 1, 4, 1, 33688, 4, 2, 1, 5),
    _NtNodeIdHex_Type()
)
ntNodeIdHex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntNodeIdHex.setStatus("current")


class _NtNodeIdString_Type(DisplayString):
    """Custom type ntNodeIdString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_NtNodeIdString_Type.__name__ = "DisplayString"
_NtNodeIdString_Object = MibTableColumn
ntNodeIdString = _NtNodeIdString_Object(
    (1, 3, 6, 1, 4, 1, 33688, 4, 2, 1, 6),
    _NtNodeIdString_Type()
)
ntNodeIdString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntNodeIdString.setStatus("current")
_NtTime_Type = DateAndTime
_NtTime_Object = MibTableColumn
ntTime = _NtTime_Object(
    (1, 3, 6, 1, 4, 1, 33688, 4, 2, 1, 7),
    _NtTime_Type()
)
ntTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntTime.setStatus("current")


class _NtUnixTime_Type(Integer32):
    """Custom type ntUnixTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_NtUnixTime_Type.__name__ = "Integer32"
_NtUnixTime_Object = MibTableColumn
ntUnixTime = _NtUnixTime_Object(
    (1, 3, 6, 1, 4, 1, 33688, 4, 2, 1, 8),
    _NtUnixTime_Type()
)
ntUnixTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntUnixTime.setStatus("current")


class _NtIso8601Time_Type(DisplayString):
    """Custom type ntIso8601Time based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NtIso8601Time_Type.__name__ = "DisplayString"
_NtIso8601Time_Object = MibTableColumn
ntIso8601Time = _NtIso8601Time_Object(
    (1, 3, 6, 1, 4, 1, 33688, 4, 2, 1, 9),
    _NtIso8601Time_Type()
)
ntIso8601Time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntIso8601Time.setStatus("current")


class _NtLinkQuality_Type(Integer32):
    """Custom type ntLinkQuality based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_NtLinkQuality_Type.__name__ = "Integer32"
_NtLinkQuality_Object = MibTableColumn
ntLinkQuality = _NtLinkQuality_Object(
    (1, 3, 6, 1, 4, 1, 33688, 4, 2, 1, 10),
    _NtLinkQuality_Type()
)
ntLinkQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntLinkQuality.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PACKETPOWER-EG4-MIB",
    **{"org": org,
       "dod": dod,
       "internet": internet,
       "private": private,
       "enterprises": enterprises,
       "packetPower": packetPower,
       "eg4": eg4,
       "readingsTable": readingsTable,
       "readingsEntry": readingsEntry,
       "reNodeId1": reNodeId1,
       "reNodeId2": reNodeId2,
       "reNodeId3": reNodeId3,
       "reNodeId4": reNodeId4,
       "channelId": channelId,
       "reNodeIdHex": reNodeIdHex,
       "reNodeIdString": reNodeIdString,
       "reChannelName": reChannelName,
       "reTime": reTime,
       "reUnixTime": reUnixTime,
       "reIso8601Time": reIso8601Time,
       "reValue": reValue,
       "reUnits": reUnits,
       "nodesTable": nodesTable,
       "nodesEntry": nodesEntry,
       "ntNodeId1": ntNodeId1,
       "ntNodeId2": ntNodeId2,
       "ntNodeId3": ntNodeId3,
       "ntNodeId4": ntNodeId4,
       "ntNodeIdHex": ntNodeIdHex,
       "ntNodeIdString": ntNodeIdString,
       "ntTime": ntTime,
       "ntUnixTime": ntUnixTime,
       "ntIso8601Time": ntIso8601Time,
       "ntLinkQuality": ntLinkQuality}
)
