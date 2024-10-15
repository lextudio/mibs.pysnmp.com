# SNMP MIB module (ZHONE-COM-IP-RIPv2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZHONE-COM-IP-RIPv2-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:20:19 2024
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

(rdIndex,) = mibBuilder.importSymbols(
    "ZHONE-COM-IP-RD-MIB",
    "rdIndex")

(zhoneIp,
 zhoneModules) = mibBuilder.importSymbols(
    "Zhone",
    "zhoneIp",
    "zhoneModules")


# MODULE-IDENTITY

comIpRip2 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 6, 52)
)
comIpRip2.setRevisions(
        ("2001-09-12 13:18",
         "2000-10-12 17:08",
         "2000-10-02 08:05",
         "2000-09-12 10:20")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class RipAuthKey(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )



# MIB Managed Objects in the order of their OIDs

_Rip2_ObjectIdentity = ObjectIdentity
rip2 = _Rip2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 2)
)
if mibBuilder.loadTexts:
    rip2.setStatus("current")
_ZhRip2GlobalTable_Object = MibTable
zhRip2GlobalTable = _ZhRip2GlobalTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 2, 1)
)
if mibBuilder.loadTexts:
    zhRip2GlobalTable.setStatus("current")
_ZhRip2GlobalEntry_Object = MibTableRow
zhRip2GlobalEntry = _ZhRip2GlobalEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 2, 1, 1)
)
zhRip2GlobalEntry.setIndexNames(
    (0, "ZHONE-COM-IP-RD-MIB", "rdIndex"),
)
if mibBuilder.loadTexts:
    zhRip2GlobalEntry.setStatus("current")
_ZhRip2GlobalRouteChanges_Type = Counter32
_ZhRip2GlobalRouteChanges_Object = MibTableColumn
zhRip2GlobalRouteChanges = _ZhRip2GlobalRouteChanges_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 2, 1, 1, 1),
    _ZhRip2GlobalRouteChanges_Type()
)
zhRip2GlobalRouteChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhRip2GlobalRouteChanges.setStatus("current")
_ZhRip2GlobalQueries_Type = Counter32
_ZhRip2GlobalQueries_Object = MibTableColumn
zhRip2GlobalQueries = _ZhRip2GlobalQueries_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 2, 1, 1, 2),
    _ZhRip2GlobalQueries_Type()
)
zhRip2GlobalQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhRip2GlobalQueries.setStatus("current")


class _ZhRip2GlobalAdminState_Type(Integer32):
    """Custom type zhRip2GlobalAdminState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_ZhRip2GlobalAdminState_Type.__name__ = "Integer32"
_ZhRip2GlobalAdminState_Object = MibTableColumn
zhRip2GlobalAdminState = _ZhRip2GlobalAdminState_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 2, 1, 1, 3),
    _ZhRip2GlobalAdminState_Type()
)
zhRip2GlobalAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhRip2GlobalAdminState.setStatus("current")


class _ZhRip2GlobalUpdateTime_Type(Unsigned32):
    """Custom type zhRip2GlobalUpdateTime based on Unsigned32"""
    defaultValue = 30


_ZhRip2GlobalUpdateTime_Object = MibTableColumn
zhRip2GlobalUpdateTime = _ZhRip2GlobalUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 2, 1, 1, 4),
    _ZhRip2GlobalUpdateTime_Type()
)
zhRip2GlobalUpdateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhRip2GlobalUpdateTime.setStatus("current")
_ZhRip2IfStatTable_Object = MibTable
zhRip2IfStatTable = _ZhRip2IfStatTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 2, 2)
)
if mibBuilder.loadTexts:
    zhRip2IfStatTable.setStatus("current")
_ZhRip2IfStatEntry_Object = MibTableRow
zhRip2IfStatEntry = _ZhRip2IfStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 2, 2, 1)
)
zhRip2IfStatEntry.setIndexNames(
    (0, "ZHONE-COM-IP-RD-MIB", "rdIndex"),
    (0, "ZHONE-COM-IP-RIPv2-MIB", "zhRip2IfStatAddress"),
)
if mibBuilder.loadTexts:
    zhRip2IfStatEntry.setStatus("current")
_ZhRip2IfStatAddress_Type = IpAddress
_ZhRip2IfStatAddress_Object = MibTableColumn
zhRip2IfStatAddress = _ZhRip2IfStatAddress_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 2, 2, 1, 1),
    _ZhRip2IfStatAddress_Type()
)
zhRip2IfStatAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhRip2IfStatAddress.setStatus("current")
_ZhRip2IfStatRcvBadPackets_Type = Counter32
_ZhRip2IfStatRcvBadPackets_Object = MibTableColumn
zhRip2IfStatRcvBadPackets = _ZhRip2IfStatRcvBadPackets_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 2, 2, 1, 2),
    _ZhRip2IfStatRcvBadPackets_Type()
)
zhRip2IfStatRcvBadPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhRip2IfStatRcvBadPackets.setStatus("current")
_ZhRip2IfStatRcvBadRoutes_Type = Counter32
_ZhRip2IfStatRcvBadRoutes_Object = MibTableColumn
zhRip2IfStatRcvBadRoutes = _ZhRip2IfStatRcvBadRoutes_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 2, 2, 1, 3),
    _ZhRip2IfStatRcvBadRoutes_Type()
)
zhRip2IfStatRcvBadRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhRip2IfStatRcvBadRoutes.setStatus("current")
_ZhRip2IfStatSentUpdates_Type = Counter32
_ZhRip2IfStatSentUpdates_Object = MibTableColumn
zhRip2IfStatSentUpdates = _ZhRip2IfStatSentUpdates_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 2, 2, 1, 4),
    _ZhRip2IfStatSentUpdates_Type()
)
zhRip2IfStatSentUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhRip2IfStatSentUpdates.setStatus("current")
_ZhRip2IfConfTable_Object = MibTable
zhRip2IfConfTable = _ZhRip2IfConfTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 2, 3)
)
if mibBuilder.loadTexts:
    zhRip2IfConfTable.setStatus("current")
_ZhRip2IfConfEntry_Object = MibTableRow
zhRip2IfConfEntry = _ZhRip2IfConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 2, 3, 1)
)
zhRip2IfConfEntry.setIndexNames(
    (0, "ZHONE-COM-IP-RD-MIB", "rdIndex"),
    (0, "ZHONE-COM-IP-RIPv2-MIB", "zhRip2IfConfAddress"),
)
if mibBuilder.loadTexts:
    zhRip2IfConfEntry.setStatus("current")
_ZhRip2IfConfAddress_Type = IpAddress
_ZhRip2IfConfAddress_Object = MibTableColumn
zhRip2IfConfAddress = _ZhRip2IfConfAddress_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 2, 3, 1, 1),
    _ZhRip2IfConfAddress_Type()
)
zhRip2IfConfAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhRip2IfConfAddress.setStatus("current")


class _ZhRip2IfConfAuthType_Type(Integer32):
    """Custom type zhRip2IfConfAuthType based on Integer32"""
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
        *(("md5", 3),
          ("noAuthentication", 1),
          ("simplePassword", 2))
    )


_ZhRip2IfConfAuthType_Type.__name__ = "Integer32"
_ZhRip2IfConfAuthType_Object = MibTableColumn
zhRip2IfConfAuthType = _ZhRip2IfConfAuthType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 2, 3, 1, 2),
    _ZhRip2IfConfAuthType_Type()
)
zhRip2IfConfAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhRip2IfConfAuthType.setStatus("current")
_ZhRip2IfConfAuthKey_Type = RipAuthKey
_ZhRip2IfConfAuthKey_Object = MibTableColumn
zhRip2IfConfAuthKey = _ZhRip2IfConfAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 2, 3, 1, 3),
    _ZhRip2IfConfAuthKey_Type()
)
zhRip2IfConfAuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhRip2IfConfAuthKey.setStatus("current")


class _ZhRip2IfConfSend_Type(Integer32):
    """Custom type zhRip2IfConfSend based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("doNotSend", 1),
          ("rip1Compatible", 3),
          ("ripV1Demand", 5),
          ("ripV2Demand", 6),
          ("ripVersion1", 2),
          ("ripVersion2", 4))
    )


_ZhRip2IfConfSend_Type.__name__ = "Integer32"
_ZhRip2IfConfSend_Object = MibTableColumn
zhRip2IfConfSend = _ZhRip2IfConfSend_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 2, 3, 1, 4),
    _ZhRip2IfConfSend_Type()
)
zhRip2IfConfSend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhRip2IfConfSend.setStatus("current")


class _ZhRip2IfConfReceive_Type(Integer32):
    """Custom type zhRip2IfConfReceive based on Integer32"""
    defaultValue = 3

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
        *(("doNotReceive", 4),
          ("rip1", 1),
          ("rip1OrRip2", 3),
          ("rip2", 2))
    )


_ZhRip2IfConfReceive_Type.__name__ = "Integer32"
_ZhRip2IfConfReceive_Object = MibTableColumn
zhRip2IfConfReceive = _ZhRip2IfConfReceive_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 2, 3, 1, 5),
    _ZhRip2IfConfReceive_Type()
)
zhRip2IfConfReceive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhRip2IfConfReceive.setStatus("current")


class _ZhRip2IfConfDefaultMetric_Type(Integer32):
    """Custom type zhRip2IfConfDefaultMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_ZhRip2IfConfDefaultMetric_Type.__name__ = "Integer32"
_ZhRip2IfConfDefaultMetric_Object = MibTableColumn
zhRip2IfConfDefaultMetric = _ZhRip2IfConfDefaultMetric_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 2, 3, 1, 6),
    _ZhRip2IfConfDefaultMetric_Type()
)
zhRip2IfConfDefaultMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhRip2IfConfDefaultMetric.setStatus("current")
_ZhRip2IfConfSrcAddress_Type = IpAddress
_ZhRip2IfConfSrcAddress_Object = MibTableColumn
zhRip2IfConfSrcAddress = _ZhRip2IfConfSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 2, 3, 1, 7),
    _ZhRip2IfConfSrcAddress_Type()
)
zhRip2IfConfSrcAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhRip2IfConfSrcAddress.setStatus("current")


class _ZhRip2IfConfStaticRouteAdvertisement_Type(Integer32):
    """Custom type zhRip2IfConfStaticRouteAdvertisement based on Integer32"""
    defaultValue = 1

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
        *(("both", 4),
          ("high", 3),
          ("low", 2),
          ("none", 1))
    )


_ZhRip2IfConfStaticRouteAdvertisement_Type.__name__ = "Integer32"
_ZhRip2IfConfStaticRouteAdvertisement_Object = MibTableColumn
zhRip2IfConfStaticRouteAdvertisement = _ZhRip2IfConfStaticRouteAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 2, 3, 1, 8),
    _ZhRip2IfConfStaticRouteAdvertisement_Type()
)
zhRip2IfConfStaticRouteAdvertisement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhRip2IfConfStaticRouteAdvertisement.setStatus("current")


class _ZhRip2IfConfPoison_Type(Integer32):
    """Custom type zhRip2IfConfPoison based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_ZhRip2IfConfPoison_Type.__name__ = "Integer32"
_ZhRip2IfConfPoison_Object = MibTableColumn
zhRip2IfConfPoison = _ZhRip2IfConfPoison_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 2, 3, 1, 9),
    _ZhRip2IfConfPoison_Type()
)
zhRip2IfConfPoison.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhRip2IfConfPoison.setStatus("current")
_ZhRip2PeerTable_Object = MibTable
zhRip2PeerTable = _ZhRip2PeerTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 2, 4)
)
if mibBuilder.loadTexts:
    zhRip2PeerTable.setStatus("current")
_ZhRip2PeerEntry_Object = MibTableRow
zhRip2PeerEntry = _ZhRip2PeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 2, 4, 1)
)
zhRip2PeerEntry.setIndexNames(
    (0, "ZHONE-COM-IP-RD-MIB", "rdIndex"),
    (0, "ZHONE-COM-IP-RIPv2-MIB", "zhRip2PeerAddress"),
)
if mibBuilder.loadTexts:
    zhRip2PeerEntry.setStatus("current")
_ZhRip2PeerAddress_Type = IpAddress
_ZhRip2PeerAddress_Object = MibTableColumn
zhRip2PeerAddress = _ZhRip2PeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 2, 4, 1, 1),
    _ZhRip2PeerAddress_Type()
)
zhRip2PeerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhRip2PeerAddress.setStatus("current")
_ZhRip2PeerLastUpdate_Type = TimeTicks
_ZhRip2PeerLastUpdate_Object = MibTableColumn
zhRip2PeerLastUpdate = _ZhRip2PeerLastUpdate_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 2, 4, 1, 2),
    _ZhRip2PeerLastUpdate_Type()
)
zhRip2PeerLastUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhRip2PeerLastUpdate.setStatus("current")


class _ZhRip2PeerVersion_Type(Integer32):
    """Custom type zhRip2PeerVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ZhRip2PeerVersion_Type.__name__ = "Integer32"
_ZhRip2PeerVersion_Object = MibTableColumn
zhRip2PeerVersion = _ZhRip2PeerVersion_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 2, 4, 1, 3),
    _ZhRip2PeerVersion_Type()
)
zhRip2PeerVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhRip2PeerVersion.setStatus("current")
_ZhRip2PeerRcvBadPackets_Type = Counter32
_ZhRip2PeerRcvBadPackets_Object = MibTableColumn
zhRip2PeerRcvBadPackets = _ZhRip2PeerRcvBadPackets_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 2, 4, 1, 4),
    _ZhRip2PeerRcvBadPackets_Type()
)
zhRip2PeerRcvBadPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhRip2PeerRcvBadPackets.setStatus("current")
_ZhRip2PeerRcvBadRoutes_Type = Counter32
_ZhRip2PeerRcvBadRoutes_Object = MibTableColumn
zhRip2PeerRcvBadRoutes = _ZhRip2PeerRcvBadRoutes_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 2, 4, 1, 5),
    _ZhRip2PeerRcvBadRoutes_Type()
)
zhRip2PeerRcvBadRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhRip2PeerRcvBadRoutes.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZHONE-COM-IP-RIPv2-MIB",
    **{"RipAuthKey": RipAuthKey,
       "rip2": rip2,
       "zhRip2GlobalTable": zhRip2GlobalTable,
       "zhRip2GlobalEntry": zhRip2GlobalEntry,
       "zhRip2GlobalRouteChanges": zhRip2GlobalRouteChanges,
       "zhRip2GlobalQueries": zhRip2GlobalQueries,
       "zhRip2GlobalAdminState": zhRip2GlobalAdminState,
       "zhRip2GlobalUpdateTime": zhRip2GlobalUpdateTime,
       "zhRip2IfStatTable": zhRip2IfStatTable,
       "zhRip2IfStatEntry": zhRip2IfStatEntry,
       "zhRip2IfStatAddress": zhRip2IfStatAddress,
       "zhRip2IfStatRcvBadPackets": zhRip2IfStatRcvBadPackets,
       "zhRip2IfStatRcvBadRoutes": zhRip2IfStatRcvBadRoutes,
       "zhRip2IfStatSentUpdates": zhRip2IfStatSentUpdates,
       "zhRip2IfConfTable": zhRip2IfConfTable,
       "zhRip2IfConfEntry": zhRip2IfConfEntry,
       "zhRip2IfConfAddress": zhRip2IfConfAddress,
       "zhRip2IfConfAuthType": zhRip2IfConfAuthType,
       "zhRip2IfConfAuthKey": zhRip2IfConfAuthKey,
       "zhRip2IfConfSend": zhRip2IfConfSend,
       "zhRip2IfConfReceive": zhRip2IfConfReceive,
       "zhRip2IfConfDefaultMetric": zhRip2IfConfDefaultMetric,
       "zhRip2IfConfSrcAddress": zhRip2IfConfSrcAddress,
       "zhRip2IfConfStaticRouteAdvertisement": zhRip2IfConfStaticRouteAdvertisement,
       "zhRip2IfConfPoison": zhRip2IfConfPoison,
       "zhRip2PeerTable": zhRip2PeerTable,
       "zhRip2PeerEntry": zhRip2PeerEntry,
       "zhRip2PeerAddress": zhRip2PeerAddress,
       "zhRip2PeerLastUpdate": zhRip2PeerLastUpdate,
       "zhRip2PeerVersion": zhRip2PeerVersion,
       "zhRip2PeerRcvBadPackets": zhRip2PeerRcvBadPackets,
       "zhRip2PeerRcvBadRoutes": zhRip2PeerRcvBadRoutes,
       "comIpRip2": comIpRip2}
)
