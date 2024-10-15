# SNMP MIB module (H3C-MCDR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/H3C-MCDR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:50:55 2024
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

h3cMultCDR = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 86)
)
h3cMultCDR.setRevisions(
        ("2007-12-15 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cMultCDRCfgObject_ObjectIdentity = ObjectIdentity
h3cMultCDRCfgObject = _H3cMultCDRCfgObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 86, 1)
)


class _H3cMultCDRStatus_Type(Integer32):
    """Custom type h3cMultCDRStatus based on Integer32"""
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


_H3cMultCDRStatus_Type.__name__ = "Integer32"
_H3cMultCDRStatus_Object = MibScalar
h3cMultCDRStatus = _H3cMultCDRStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 86, 1, 1),
    _H3cMultCDRStatus_Type()
)
h3cMultCDRStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cMultCDRStatus.setStatus("current")


class _H3cMultCDRReportInterval_Type(Integer32):
    """Custom type h3cMultCDRReportInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 600),
    )


_H3cMultCDRReportInterval_Type.__name__ = "Integer32"
_H3cMultCDRReportInterval_Object = MibScalar
h3cMultCDRReportInterval = _H3cMultCDRReportInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 86, 1, 2),
    _H3cMultCDRReportInterval_Type()
)
h3cMultCDRReportInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cMultCDRReportInterval.setStatus("current")


class _H3cMultCDRCacheLimit_Type(Integer32):
    """Custom type h3cMultCDRCacheLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1024),
    )


_H3cMultCDRCacheLimit_Type.__name__ = "Integer32"
_H3cMultCDRCacheLimit_Object = MibScalar
h3cMultCDRCacheLimit = _H3cMultCDRCacheLimit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 86, 1, 3),
    _H3cMultCDRCacheLimit_Type()
)
h3cMultCDRCacheLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cMultCDRCacheLimit.setStatus("current")


class _H3cMultCDRRecordDelay_Type(Integer32):
    """Custom type h3cMultCDRRecordDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 600),
    )


_H3cMultCDRRecordDelay_Type.__name__ = "Integer32"
_H3cMultCDRRecordDelay_Object = MibScalar
h3cMultCDRRecordDelay = _H3cMultCDRRecordDelay_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 86, 1, 4),
    _H3cMultCDRRecordDelay_Type()
)
h3cMultCDRRecordDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cMultCDRRecordDelay.setStatus("current")


class _H3cMultCDRRecordSend_Type(Integer32):
    """Custom type h3cMultCDRRecordSend based on Integer32"""
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


_H3cMultCDRRecordSend_Type.__name__ = "Integer32"
_H3cMultCDRRecordSend_Object = MibScalar
h3cMultCDRRecordSend = _H3cMultCDRRecordSend_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 86, 1, 5),
    _H3cMultCDRRecordSend_Type()
)
h3cMultCDRRecordSend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cMultCDRRecordSend.setStatus("current")
_H3cMultUserOnlineInfoTable_Object = MibTable
h3cMultUserOnlineInfoTable = _H3cMultUserOnlineInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 86, 2)
)
if mibBuilder.loadTexts:
    h3cMultUserOnlineInfoTable.setStatus("current")
_H3cMultUserOnlineInfoEntry_Object = MibTableRow
h3cMultUserOnlineInfoEntry = _H3cMultUserOnlineInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 86, 2, 1)
)
h3cMultUserOnlineInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "H3C-MCDR-MIB", "h3cMultUserRecordID"),
)
if mibBuilder.loadTexts:
    h3cMultUserOnlineInfoEntry.setStatus("current")
_H3cMultUserRecordID_Type = Unsigned32
_H3cMultUserRecordID_Object = MibTableColumn
h3cMultUserRecordID = _H3cMultUserRecordID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 86, 2, 1, 1),
    _H3cMultUserRecordID_Type()
)
h3cMultUserRecordID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cMultUserRecordID.setStatus("current")
_H3cMultUserSubIfIndex_Type = Unsigned32
_H3cMultUserSubIfIndex_Object = MibTableColumn
h3cMultUserSubIfIndex = _H3cMultUserSubIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 86, 2, 1, 2),
    _H3cMultUserSubIfIndex_Type()
)
h3cMultUserSubIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMultUserSubIfIndex.setStatus("current")
_H3cMultUserVlanID_Type = VlanId
_H3cMultUserVlanID_Object = MibTableColumn
h3cMultUserVlanID = _H3cMultUserVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 86, 2, 1, 3),
    _H3cMultUserVlanID_Type()
)
h3cMultUserVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMultUserVlanID.setStatus("current")
_H3cMultUserJoinGAddrType_Type = InetAddressType
_H3cMultUserJoinGAddrType_Object = MibTableColumn
h3cMultUserJoinGAddrType = _H3cMultUserJoinGAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 86, 2, 1, 4),
    _H3cMultUserJoinGAddrType_Type()
)
h3cMultUserJoinGAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMultUserJoinGAddrType.setStatus("current")
_H3cMultUserJoinGAddr_Type = InetAddress
_H3cMultUserJoinGAddr_Object = MibTableColumn
h3cMultUserJoinGAddr = _H3cMultUserJoinGAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 86, 2, 1, 5),
    _H3cMultUserJoinGAddr_Type()
)
h3cMultUserJoinGAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMultUserJoinGAddr.setStatus("current")
_H3cMultUserJoinSAddrType_Type = InetAddressType
_H3cMultUserJoinSAddrType_Object = MibTableColumn
h3cMultUserJoinSAddrType = _H3cMultUserJoinSAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 86, 2, 1, 6),
    _H3cMultUserJoinSAddrType_Type()
)
h3cMultUserJoinSAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMultUserJoinSAddrType.setStatus("current")
_H3cMultUserJoinSAddr_Type = InetAddress
_H3cMultUserJoinSAddr_Object = MibTableColumn
h3cMultUserJoinSAddr = _H3cMultUserJoinSAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 86, 2, 1, 7),
    _H3cMultUserJoinSAddr_Type()
)
h3cMultUserJoinSAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMultUserJoinSAddr.setStatus("current")


class _H3cMultUserStatus_Type(Integer32):
    """Custom type h3cMultUserStatus based on Integer32"""
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


_H3cMultUserStatus_Type.__name__ = "Integer32"
_H3cMultUserStatus_Object = MibTableColumn
h3cMultUserStatus = _H3cMultUserStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 86, 2, 1, 8),
    _H3cMultUserStatus_Type()
)
h3cMultUserStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMultUserStatus.setStatus("current")
_H3cMultUserJoinTime_Type = DateAndTime
_H3cMultUserJoinTime_Object = MibTableColumn
h3cMultUserJoinTime = _H3cMultUserJoinTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 86, 2, 1, 9),
    _H3cMultUserJoinTime_Type()
)
h3cMultUserJoinTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMultUserJoinTime.setStatus("current")
_H3cMultUserPreviewTimes_Type = Unsigned32
_H3cMultUserPreviewTimes_Object = MibTableColumn
h3cMultUserPreviewTimes = _H3cMultUserPreviewTimes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 86, 2, 1, 10),
    _H3cMultUserPreviewTimes_Type()
)
h3cMultUserPreviewTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMultUserPreviewTimes.setStatus("current")
_H3cMultUserPreviewRemain_Type = Unsigned32
_H3cMultUserPreviewRemain_Object = MibTableColumn
h3cMultUserPreviewRemain = _H3cMultUserPreviewRemain_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 86, 2, 1, 11),
    _H3cMultUserPreviewRemain_Type()
)
h3cMultUserPreviewRemain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMultUserPreviewRemain.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-MCDR-MIB",
    **{"h3cMultCDR": h3cMultCDR,
       "h3cMultCDRCfgObject": h3cMultCDRCfgObject,
       "h3cMultCDRStatus": h3cMultCDRStatus,
       "h3cMultCDRReportInterval": h3cMultCDRReportInterval,
       "h3cMultCDRCacheLimit": h3cMultCDRCacheLimit,
       "h3cMultCDRRecordDelay": h3cMultCDRRecordDelay,
       "h3cMultCDRRecordSend": h3cMultCDRRecordSend,
       "h3cMultUserOnlineInfoTable": h3cMultUserOnlineInfoTable,
       "h3cMultUserOnlineInfoEntry": h3cMultUserOnlineInfoEntry,
       "h3cMultUserRecordID": h3cMultUserRecordID,
       "h3cMultUserSubIfIndex": h3cMultUserSubIfIndex,
       "h3cMultUserVlanID": h3cMultUserVlanID,
       "h3cMultUserJoinGAddrType": h3cMultUserJoinGAddrType,
       "h3cMultUserJoinGAddr": h3cMultUserJoinGAddr,
       "h3cMultUserJoinSAddrType": h3cMultUserJoinSAddrType,
       "h3cMultUserJoinSAddr": h3cMultUserJoinSAddr,
       "h3cMultUserStatus": h3cMultUserStatus,
       "h3cMultUserJoinTime": h3cMultUserJoinTime,
       "h3cMultUserPreviewTimes": h3cMultUserPreviewTimes,
       "h3cMultUserPreviewRemain": h3cMultUserPreviewRemain}
)
