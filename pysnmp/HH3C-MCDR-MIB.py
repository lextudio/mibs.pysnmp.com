# SNMP MIB module (HH3C-MCDR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-MCDR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:54:05 2024
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(VlanId,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

hh3cMultCDR = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 86)
)
hh3cMultCDR.setRevisions(
        ("2007-12-15 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cMultCDRCfgObject_ObjectIdentity = ObjectIdentity
hh3cMultCDRCfgObject = _Hh3cMultCDRCfgObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 86, 1)
)


class _Hh3cMultCDRStatus_Type(Integer32):
    """Custom type hh3cMultCDRStatus based on Integer32"""
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


_Hh3cMultCDRStatus_Type.__name__ = "Integer32"
_Hh3cMultCDRStatus_Object = MibScalar
hh3cMultCDRStatus = _Hh3cMultCDRStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 86, 1, 1),
    _Hh3cMultCDRStatus_Type()
)
hh3cMultCDRStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cMultCDRStatus.setStatus("current")


class _Hh3cMultCDRReportInterval_Type(Integer32):
    """Custom type hh3cMultCDRReportInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 600),
    )


_Hh3cMultCDRReportInterval_Type.__name__ = "Integer32"
_Hh3cMultCDRReportInterval_Object = MibScalar
hh3cMultCDRReportInterval = _Hh3cMultCDRReportInterval_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 86, 1, 2),
    _Hh3cMultCDRReportInterval_Type()
)
hh3cMultCDRReportInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cMultCDRReportInterval.setStatus("current")


class _Hh3cMultCDRCacheLimit_Type(Integer32):
    """Custom type hh3cMultCDRCacheLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1024),
    )


_Hh3cMultCDRCacheLimit_Type.__name__ = "Integer32"
_Hh3cMultCDRCacheLimit_Object = MibScalar
hh3cMultCDRCacheLimit = _Hh3cMultCDRCacheLimit_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 86, 1, 3),
    _Hh3cMultCDRCacheLimit_Type()
)
hh3cMultCDRCacheLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cMultCDRCacheLimit.setStatus("current")


class _Hh3cMultCDRRecordDelay_Type(Integer32):
    """Custom type hh3cMultCDRRecordDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 600),
    )


_Hh3cMultCDRRecordDelay_Type.__name__ = "Integer32"
_Hh3cMultCDRRecordDelay_Object = MibScalar
hh3cMultCDRRecordDelay = _Hh3cMultCDRRecordDelay_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 86, 1, 4),
    _Hh3cMultCDRRecordDelay_Type()
)
hh3cMultCDRRecordDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cMultCDRRecordDelay.setStatus("current")


class _Hh3cMultCDRRecordSend_Type(Integer32):
    """Custom type hh3cMultCDRRecordSend based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("caching", 2),
          ("send", 1))
    )


_Hh3cMultCDRRecordSend_Type.__name__ = "Integer32"
_Hh3cMultCDRRecordSend_Object = MibScalar
hh3cMultCDRRecordSend = _Hh3cMultCDRRecordSend_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 86, 1, 5),
    _Hh3cMultCDRRecordSend_Type()
)
hh3cMultCDRRecordSend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cMultCDRRecordSend.setStatus("current")
_Hh3cMultUserOnlineInfoTable_Object = MibTable
hh3cMultUserOnlineInfoTable = _Hh3cMultUserOnlineInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 86, 2)
)
if mibBuilder.loadTexts:
    hh3cMultUserOnlineInfoTable.setStatus("current")
_Hh3cMultUserOnlineInfoEntry_Object = MibTableRow
hh3cMultUserOnlineInfoEntry = _Hh3cMultUserOnlineInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 86, 2, 1)
)
hh3cMultUserOnlineInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-MCDR-MIB", "hh3cMultUserRecordID"),
)
if mibBuilder.loadTexts:
    hh3cMultUserOnlineInfoEntry.setStatus("current")
_Hh3cMultUserRecordID_Type = Unsigned32
_Hh3cMultUserRecordID_Object = MibTableColumn
hh3cMultUserRecordID = _Hh3cMultUserRecordID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 86, 2, 1, 1),
    _Hh3cMultUserRecordID_Type()
)
hh3cMultUserRecordID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cMultUserRecordID.setStatus("current")
_Hh3cMultUserSubIfIndex_Type = Unsigned32
_Hh3cMultUserSubIfIndex_Object = MibTableColumn
hh3cMultUserSubIfIndex = _Hh3cMultUserSubIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 86, 2, 1, 2),
    _Hh3cMultUserSubIfIndex_Type()
)
hh3cMultUserSubIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMultUserSubIfIndex.setStatus("current")
_Hh3cMultUserVlanID_Type = VlanId
_Hh3cMultUserVlanID_Object = MibTableColumn
hh3cMultUserVlanID = _Hh3cMultUserVlanID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 86, 2, 1, 3),
    _Hh3cMultUserVlanID_Type()
)
hh3cMultUserVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMultUserVlanID.setStatus("current")
_Hh3cMultUserJoinGAddrType_Type = InetAddressType
_Hh3cMultUserJoinGAddrType_Object = MibTableColumn
hh3cMultUserJoinGAddrType = _Hh3cMultUserJoinGAddrType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 86, 2, 1, 4),
    _Hh3cMultUserJoinGAddrType_Type()
)
hh3cMultUserJoinGAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMultUserJoinGAddrType.setStatus("current")
_Hh3cMultUserJoinGAddr_Type = InetAddress
_Hh3cMultUserJoinGAddr_Object = MibTableColumn
hh3cMultUserJoinGAddr = _Hh3cMultUserJoinGAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 86, 2, 1, 5),
    _Hh3cMultUserJoinGAddr_Type()
)
hh3cMultUserJoinGAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMultUserJoinGAddr.setStatus("current")
_Hh3cMultUserJoinSAddrType_Type = InetAddressType
_Hh3cMultUserJoinSAddrType_Object = MibTableColumn
hh3cMultUserJoinSAddrType = _Hh3cMultUserJoinSAddrType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 86, 2, 1, 6),
    _Hh3cMultUserJoinSAddrType_Type()
)
hh3cMultUserJoinSAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMultUserJoinSAddrType.setStatus("current")
_Hh3cMultUserJoinSAddr_Type = InetAddress
_Hh3cMultUserJoinSAddr_Object = MibTableColumn
hh3cMultUserJoinSAddr = _Hh3cMultUserJoinSAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 86, 2, 1, 7),
    _Hh3cMultUserJoinSAddr_Type()
)
hh3cMultUserJoinSAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMultUserJoinSAddr.setStatus("current")


class _Hh3cMultUserStatus_Type(Integer32):
    """Custom type hh3cMultUserStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("permit", 1),
          ("preview", 2))
    )


_Hh3cMultUserStatus_Type.__name__ = "Integer32"
_Hh3cMultUserStatus_Object = MibTableColumn
hh3cMultUserStatus = _Hh3cMultUserStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 86, 2, 1, 8),
    _Hh3cMultUserStatus_Type()
)
hh3cMultUserStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMultUserStatus.setStatus("current")
_Hh3cMultUserJoinTime_Type = DateAndTime
_Hh3cMultUserJoinTime_Object = MibTableColumn
hh3cMultUserJoinTime = _Hh3cMultUserJoinTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 86, 2, 1, 9),
    _Hh3cMultUserJoinTime_Type()
)
hh3cMultUserJoinTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMultUserJoinTime.setStatus("current")
_Hh3cMultUserPreviewTimes_Type = Unsigned32
_Hh3cMultUserPreviewTimes_Object = MibTableColumn
hh3cMultUserPreviewTimes = _Hh3cMultUserPreviewTimes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 86, 2, 1, 10),
    _Hh3cMultUserPreviewTimes_Type()
)
hh3cMultUserPreviewTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMultUserPreviewTimes.setStatus("current")
_Hh3cMultUserPreviewRemain_Type = Unsigned32
_Hh3cMultUserPreviewRemain_Object = MibTableColumn
hh3cMultUserPreviewRemain = _Hh3cMultUserPreviewRemain_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 86, 2, 1, 11),
    _Hh3cMultUserPreviewRemain_Type()
)
hh3cMultUserPreviewRemain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMultUserPreviewRemain.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-MCDR-MIB",
    **{"hh3cMultCDR": hh3cMultCDR,
       "hh3cMultCDRCfgObject": hh3cMultCDRCfgObject,
       "hh3cMultCDRStatus": hh3cMultCDRStatus,
       "hh3cMultCDRReportInterval": hh3cMultCDRReportInterval,
       "hh3cMultCDRCacheLimit": hh3cMultCDRCacheLimit,
       "hh3cMultCDRRecordDelay": hh3cMultCDRRecordDelay,
       "hh3cMultCDRRecordSend": hh3cMultCDRRecordSend,
       "hh3cMultUserOnlineInfoTable": hh3cMultUserOnlineInfoTable,
       "hh3cMultUserOnlineInfoEntry": hh3cMultUserOnlineInfoEntry,
       "hh3cMultUserRecordID": hh3cMultUserRecordID,
       "hh3cMultUserSubIfIndex": hh3cMultUserSubIfIndex,
       "hh3cMultUserVlanID": hh3cMultUserVlanID,
       "hh3cMultUserJoinGAddrType": hh3cMultUserJoinGAddrType,
       "hh3cMultUserJoinGAddr": hh3cMultUserJoinGAddr,
       "hh3cMultUserJoinSAddrType": hh3cMultUserJoinSAddrType,
       "hh3cMultUserJoinSAddr": hh3cMultUserJoinSAddr,
       "hh3cMultUserStatus": hh3cMultUserStatus,
       "hh3cMultUserJoinTime": hh3cMultUserJoinTime,
       "hh3cMultUserPreviewTimes": hh3cMultUserPreviewTimes,
       "hh3cMultUserPreviewRemain": hh3cMultUserPreviewRemain}
)
