# SNMP MIB module (HPN-ICF-MCDR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-MCDR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:01:04 2024
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

hpnicfMultCDR = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 86)
)
hpnicfMultCDR.setRevisions(
        ("2007-12-15 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfMultCDRCfgObject_ObjectIdentity = ObjectIdentity
hpnicfMultCDRCfgObject = _HpnicfMultCDRCfgObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 86, 1)
)


class _HpnicfMultCDRStatus_Type(Integer32):
    """Custom type hpnicfMultCDRStatus based on Integer32"""
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


_HpnicfMultCDRStatus_Type.__name__ = "Integer32"
_HpnicfMultCDRStatus_Object = MibScalar
hpnicfMultCDRStatus = _HpnicfMultCDRStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 86, 1, 1),
    _HpnicfMultCDRStatus_Type()
)
hpnicfMultCDRStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfMultCDRStatus.setStatus("current")


class _HpnicfMultCDRReportInterval_Type(Integer32):
    """Custom type hpnicfMultCDRReportInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 600),
    )


_HpnicfMultCDRReportInterval_Type.__name__ = "Integer32"
_HpnicfMultCDRReportInterval_Object = MibScalar
hpnicfMultCDRReportInterval = _HpnicfMultCDRReportInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 86, 1, 2),
    _HpnicfMultCDRReportInterval_Type()
)
hpnicfMultCDRReportInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfMultCDRReportInterval.setStatus("current")


class _HpnicfMultCDRCacheLimit_Type(Integer32):
    """Custom type hpnicfMultCDRCacheLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1024),
    )


_HpnicfMultCDRCacheLimit_Type.__name__ = "Integer32"
_HpnicfMultCDRCacheLimit_Object = MibScalar
hpnicfMultCDRCacheLimit = _HpnicfMultCDRCacheLimit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 86, 1, 3),
    _HpnicfMultCDRCacheLimit_Type()
)
hpnicfMultCDRCacheLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfMultCDRCacheLimit.setStatus("current")


class _HpnicfMultCDRRecordDelay_Type(Integer32):
    """Custom type hpnicfMultCDRRecordDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 600),
    )


_HpnicfMultCDRRecordDelay_Type.__name__ = "Integer32"
_HpnicfMultCDRRecordDelay_Object = MibScalar
hpnicfMultCDRRecordDelay = _HpnicfMultCDRRecordDelay_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 86, 1, 4),
    _HpnicfMultCDRRecordDelay_Type()
)
hpnicfMultCDRRecordDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfMultCDRRecordDelay.setStatus("current")


class _HpnicfMultCDRRecordSend_Type(Integer32):
    """Custom type hpnicfMultCDRRecordSend based on Integer32"""
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


_HpnicfMultCDRRecordSend_Type.__name__ = "Integer32"
_HpnicfMultCDRRecordSend_Object = MibScalar
hpnicfMultCDRRecordSend = _HpnicfMultCDRRecordSend_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 86, 1, 5),
    _HpnicfMultCDRRecordSend_Type()
)
hpnicfMultCDRRecordSend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfMultCDRRecordSend.setStatus("current")
_HpnicfMultUserOnlineInfoTable_Object = MibTable
hpnicfMultUserOnlineInfoTable = _HpnicfMultUserOnlineInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 86, 2)
)
if mibBuilder.loadTexts:
    hpnicfMultUserOnlineInfoTable.setStatus("current")
_HpnicfMultUserOnlineInfoEntry_Object = MibTableRow
hpnicfMultUserOnlineInfoEntry = _HpnicfMultUserOnlineInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 86, 2, 1)
)
hpnicfMultUserOnlineInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HPN-ICF-MCDR-MIB", "hpnicfMultUserRecordID"),
)
if mibBuilder.loadTexts:
    hpnicfMultUserOnlineInfoEntry.setStatus("current")
_HpnicfMultUserRecordID_Type = Unsigned32
_HpnicfMultUserRecordID_Object = MibTableColumn
hpnicfMultUserRecordID = _HpnicfMultUserRecordID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 86, 2, 1, 1),
    _HpnicfMultUserRecordID_Type()
)
hpnicfMultUserRecordID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfMultUserRecordID.setStatus("current")
_HpnicfMultUserSubIfIndex_Type = Unsigned32
_HpnicfMultUserSubIfIndex_Object = MibTableColumn
hpnicfMultUserSubIfIndex = _HpnicfMultUserSubIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 86, 2, 1, 2),
    _HpnicfMultUserSubIfIndex_Type()
)
hpnicfMultUserSubIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMultUserSubIfIndex.setStatus("current")
_HpnicfMultUserVlanID_Type = VlanId
_HpnicfMultUserVlanID_Object = MibTableColumn
hpnicfMultUserVlanID = _HpnicfMultUserVlanID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 86, 2, 1, 3),
    _HpnicfMultUserVlanID_Type()
)
hpnicfMultUserVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMultUserVlanID.setStatus("current")
_HpnicfMultUserJoinGAddrType_Type = InetAddressType
_HpnicfMultUserJoinGAddrType_Object = MibTableColumn
hpnicfMultUserJoinGAddrType = _HpnicfMultUserJoinGAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 86, 2, 1, 4),
    _HpnicfMultUserJoinGAddrType_Type()
)
hpnicfMultUserJoinGAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMultUserJoinGAddrType.setStatus("current")
_HpnicfMultUserJoinGAddr_Type = InetAddress
_HpnicfMultUserJoinGAddr_Object = MibTableColumn
hpnicfMultUserJoinGAddr = _HpnicfMultUserJoinGAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 86, 2, 1, 5),
    _HpnicfMultUserJoinGAddr_Type()
)
hpnicfMultUserJoinGAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMultUserJoinGAddr.setStatus("current")
_HpnicfMultUserJoinSAddrType_Type = InetAddressType
_HpnicfMultUserJoinSAddrType_Object = MibTableColumn
hpnicfMultUserJoinSAddrType = _HpnicfMultUserJoinSAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 86, 2, 1, 6),
    _HpnicfMultUserJoinSAddrType_Type()
)
hpnicfMultUserJoinSAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMultUserJoinSAddrType.setStatus("current")
_HpnicfMultUserJoinSAddr_Type = InetAddress
_HpnicfMultUserJoinSAddr_Object = MibTableColumn
hpnicfMultUserJoinSAddr = _HpnicfMultUserJoinSAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 86, 2, 1, 7),
    _HpnicfMultUserJoinSAddr_Type()
)
hpnicfMultUserJoinSAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMultUserJoinSAddr.setStatus("current")


class _HpnicfMultUserStatus_Type(Integer32):
    """Custom type hpnicfMultUserStatus based on Integer32"""
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


_HpnicfMultUserStatus_Type.__name__ = "Integer32"
_HpnicfMultUserStatus_Object = MibTableColumn
hpnicfMultUserStatus = _HpnicfMultUserStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 86, 2, 1, 8),
    _HpnicfMultUserStatus_Type()
)
hpnicfMultUserStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMultUserStatus.setStatus("current")
_HpnicfMultUserJoinTime_Type = DateAndTime
_HpnicfMultUserJoinTime_Object = MibTableColumn
hpnicfMultUserJoinTime = _HpnicfMultUserJoinTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 86, 2, 1, 9),
    _HpnicfMultUserJoinTime_Type()
)
hpnicfMultUserJoinTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMultUserJoinTime.setStatus("current")
_HpnicfMultUserPreviewTimes_Type = Unsigned32
_HpnicfMultUserPreviewTimes_Object = MibTableColumn
hpnicfMultUserPreviewTimes = _HpnicfMultUserPreviewTimes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 86, 2, 1, 10),
    _HpnicfMultUserPreviewTimes_Type()
)
hpnicfMultUserPreviewTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMultUserPreviewTimes.setStatus("current")
_HpnicfMultUserPreviewRemain_Type = Unsigned32
_HpnicfMultUserPreviewRemain_Object = MibTableColumn
hpnicfMultUserPreviewRemain = _HpnicfMultUserPreviewRemain_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 86, 2, 1, 11),
    _HpnicfMultUserPreviewRemain_Type()
)
hpnicfMultUserPreviewRemain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMultUserPreviewRemain.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-MCDR-MIB",
    **{"hpnicfMultCDR": hpnicfMultCDR,
       "hpnicfMultCDRCfgObject": hpnicfMultCDRCfgObject,
       "hpnicfMultCDRStatus": hpnicfMultCDRStatus,
       "hpnicfMultCDRReportInterval": hpnicfMultCDRReportInterval,
       "hpnicfMultCDRCacheLimit": hpnicfMultCDRCacheLimit,
       "hpnicfMultCDRRecordDelay": hpnicfMultCDRRecordDelay,
       "hpnicfMultCDRRecordSend": hpnicfMultCDRRecordSend,
       "hpnicfMultUserOnlineInfoTable": hpnicfMultUserOnlineInfoTable,
       "hpnicfMultUserOnlineInfoEntry": hpnicfMultUserOnlineInfoEntry,
       "hpnicfMultUserRecordID": hpnicfMultUserRecordID,
       "hpnicfMultUserSubIfIndex": hpnicfMultUserSubIfIndex,
       "hpnicfMultUserVlanID": hpnicfMultUserVlanID,
       "hpnicfMultUserJoinGAddrType": hpnicfMultUserJoinGAddrType,
       "hpnicfMultUserJoinGAddr": hpnicfMultUserJoinGAddr,
       "hpnicfMultUserJoinSAddrType": hpnicfMultUserJoinSAddrType,
       "hpnicfMultUserJoinSAddr": hpnicfMultUserJoinSAddr,
       "hpnicfMultUserStatus": hpnicfMultUserStatus,
       "hpnicfMultUserJoinTime": hpnicfMultUserJoinTime,
       "hpnicfMultUserPreviewTimes": hpnicfMultUserPreviewTimes,
       "hpnicfMultUserPreviewRemain": hpnicfMultUserPreviewRemain}
)
